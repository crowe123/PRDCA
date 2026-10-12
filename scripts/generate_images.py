#!/usr/bin/env python3
"""Generate the site's photos with the kie.ai Nano Banana model.

Usage:  KIE_API_KEY=... python3 scripts/generate_images.py [name ...]

Prompts live in data/image_prompts.json. Images are saved to static/img/<name>.jpg
(converted with Pillow when available, otherwise kept as the PNG kie.ai returns).
Existing files are skipped; pass names to regenerate specific images.
"""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "img"
API = "https://api.kie.ai/api/v1/jobs"
MODEL = "google/nano-banana"


def call(method, url, key, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def generate(name, spec, key):
    task = call("POST", f"{API}/createTask", key, {"model": MODEL, "input": {
        "prompt": spec["prompt"], "output_format": "png", "image_size": spec.get("size", "3:2")}})
    if task.get("code") != 200:
        return f"{name}: create failed: {task}"
    task_id = task["data"]["taskId"]
    for _ in range(90):
        time.sleep(5)
        info = call("GET", f"{API}/recordInfo?taskId={task_id}", key)["data"]
        if info["state"] == "success":
            url = json.loads(info["resultJson"])["resultUrls"][0]
            raw = urllib.request.urlopen(url, timeout=120).read()
            png = OUT / f"{name}.png"
            png.write_bytes(raw)
            try:
                from PIL import Image
                img = Image.open(png).convert("RGB")
                img.thumbnail((1600, 1600))
                img.save(OUT / f"{name}.jpg", quality=82, optimize=True, progressive=True)
                png.unlink()
            except ImportError:
                pass
            return f"{name}: saved"
        if info["state"] == "fail":
            return f"{name}: failed: {info.get('failMsg')}"
    return f"{name}: timed out"


def main():
    key = os.environ.get("KIE_API_KEY")
    if not key:
        sys.exit("Set KIE_API_KEY")
    OUT.mkdir(parents=True, exist_ok=True)
    prompts = json.loads((ROOT / "data" / "image_prompts.json").read_text())
    names = sys.argv[1:] or [n for n in prompts
                             if not any((OUT / f"{n}.{e}").exists() for e in ("jpg", "png"))]
    with ThreadPoolExecutor(4) as pool:
        for line in pool.map(lambda n: generate(n, prompts[n], key), names):
            print(line, flush=True)


if __name__ == "__main__":
    main()
