const json = (body, status = 200) => new Response(JSON.stringify(body), {
  status,
  headers: {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
  },
});

export async function onRequestPost({ request, env }) {
  if (!env.N8N_LEAD_WEBHOOK_URL) {
    return json({ error: "Enquiry service is not configured" }, 503);
  }

  const type = request.headers.get("content-type") || "";
  if (!type.includes("application/json")) {
    return json({ error: "JSON required" }, 415);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "Invalid request" }, 400);
  }

  // Honeypot: pretend success so simple bots do not learn the rejection rule.
  if (body.website) return json({ ok: true });

  const clean = (value, max = 2000) => String(value ?? "").trim().slice(0, max);
  const payload = {
    source: "website",
    customer_name: clean(body.customer_name, 120),
    phone: clean(body.phone, 60),
    email: clean(body.email, 160),
    job_address: clean(body.job_address, 240),
    service: clean(body.service, 120),
    customer_type: clean(body.customer_type, 80),
    measurements: clean(body.measurements, 160),
    preferred_timing: clean(body.preferred_timing, 160),
    message: clean(body.message, 3000),
    privacy_consent: body.privacy_consent === "yes",
  };

  if (
    !payload.customer_name ||
    !payload.phone ||
    !payload.job_address ||
    !payload.service ||
    !payload.message ||
    !payload.privacy_consent
  ) {
    return json({ error: "Missing required fields" }, 400);
  }

  let upstream;
  try {
    upstream = await fetch(env.N8N_LEAD_WEBHOOK_URL, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-voila-source": "website",
      },
      body: JSON.stringify(payload),
    });
  } catch {
    return json({ error: "Enquiry workflow unavailable" }, 502);
  }

  if (!upstream.ok) {
    return json({ error: "Enquiry workflow unavailable" }, 502);
  }

  return json({ ok: true });
}

export function onRequest() {
  return json({ error: "Method not allowed" }, 405);
}
