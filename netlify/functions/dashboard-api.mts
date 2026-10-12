import type { Config } from "@netlify/functions"
import { getStore } from "@netlify/blobs"
import siteData from "../../data/dashboard.json" with { type: "json" }

// Private API behind the /dashboard/ page. Every request must carry the
// DASHBOARD_KEY environment variable in the x-dashboard-key header.
//   GET  -> site tracker, contractor pipeline (with saved statuses) and referral events
//   POST -> save one pipeline status: { id, status, note }
const STATUSES = new Set(["Open", "Done", "To call", "No answer", "Verified", "Not offering pool removal", "Listed", "Rejected"])

function authorised(req: Request) {
  const key = Netlify.env.get("DASHBOARD_KEY")
  return Boolean(key) && req.headers.get("x-dashboard-key") === key
}

export default async (req: Request) => {
  if (!authorised(req)) return new Response("Unauthorised", { status: 401 })
  const pipeline = getStore({ name: "contractor-pipeline", consistency: "strong" })

  if (req.method === "POST") {
    const { id, status, note } = await req.json().catch(() => ({}))
    if (typeof id !== "string" || !id || id.length > 200 || !STATUSES.has(status)) {
      return new Response("Bad request", { status: 400 })
    }
    const saved = { status, note: typeof note === "string" ? note.slice(0, 500) : "", updated: new Date().toISOString() }
    await pipeline.setJSON(id, saved)
    return Response.json(saved)
  }

  const days = Math.min(Number(new URL(req.url).searchParams.get("days")) || 90, 365)
  const since = new Date(Date.now() - days * 864e5).toISOString().slice(0, 10)
  const events = getStore("referral-events")
  const { blobs } = await events.list()
  const recent = blobs.filter((b) => b.key.slice(0, 10) >= since)
  const eventData = (await Promise.all(recent.map((b) => events.get(b.key, { type: "json" })))).filter(Boolean)

  const { blobs: saved } = await pipeline.list()
  const statuses: Record<string, unknown> = {}
  await Promise.all(saved.map(async (b) => { statuses[b.key] = await pipeline.get(b.key, { type: "json" }) }))

  return Response.json({ ...siteData, statuses, events: eventData, days })
}

export const config: Config = { path: "/api/dashboard", method: ["GET", "POST"] }
