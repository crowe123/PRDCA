import type { Config, Context } from "@netlify/functions"
import { getStore } from "@netlify/blobs"

// Records referral events from the public site: taps on a phone link and
// referral form submissions. One blob per event (no read-modify-write).
const TYPES = new Set(["call", "form"])

const clip = (v: unknown, n = 120) => (typeof v === "string" ? v.slice(0, n) : "")

export default async (req: Request, context: Context) => {
  let body: Record<string, unknown>
  try {
    body = await req.json()
  } catch {
    return new Response("Bad request", { status: 400 })
  }
  const type = clip(body.type, 10)
  if (!TYPES.has(type)) return new Response("Bad request", { status: 400 })

  const at = new Date().toISOString()
  const event = {
    type,
    at,
    page: clip(body.page, 200),
    city: clip(body.city, 60),
    // call: who was called (a listed contractor, or the site's own number)
    target: clip(body.target, 120),
    phone: clip(body.phone, 30),
    // form: request details without the visitor's personal data
    poolType: clip(body.poolType, 40),
    method: clip(body.method, 40),
    visitorRegion: context.geo?.subdivision?.code ?? "",
  }
  const key = `${at.slice(0, 10)}/${at}-${crypto.randomUUID().slice(0, 8)}`
  await getStore("referral-events").setJSON(key, event)
  return new Response(null, { status: 204 })
}

export const config: Config = {
  path: "/api/track",
  method: "POST",
  rateLimit: { windowLimit: 30, windowSize: 60, aggregateBy: ["ip", "domain"] },
}
