const PFQ_ID = /^PFQ-([a-z0-9_]+)-(\d{9})$/i;

function json(body, status = 200, headers = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      ...headers,
    },
  });
}

function allowedOrigins(env) {
  return String(env.PUBLIC_ORIGINS || "")
    .split(",")
    .map((value) => value.trim())
    .filter(Boolean);
}

function corsHeaders(request, env) {
  const origin = request.headers.get("origin") || "";
  const allowed = allowedOrigins(env);
  if (!origin || !allowed.includes(origin)) return {};
  return {
    "access-control-allow-origin": origin,
    "access-control-allow-methods": "POST, OPTIONS",
    "access-control-allow-headers": "content-type",
    "access-control-max-age": "86400",
    vary: "Origin",
  };
}

function requireAdmin(request, env) {
  const token = String(env.ADMIN_TOKEN || "");
  const auth = request.headers.get("authorization") || "";
  return Boolean(token) && auth === `Bearer ${token}`;
}

function cleanText(value, maxLength) {
  return String(value ?? "").trim().slice(0, maxLength);
}

async function submitReport(request, env) {
  const cors = corsHeaders(request, env);
  const origin = request.headers.get("origin") || "";
  if (origin && !cors["access-control-allow-origin"]) {
    return json({ error: "Origin is not allowed" }, 403);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "JSON body is required" }, 400, cors);
  }

  const questionId = cleanText(body.question_id, 96);
  const match = PFQ_ID.exec(questionId);
  if (!match) {
    return json({ error: "A stable PFQ question ID is required" }, 400, cors);
  }

  const now = new Date().toISOString();
  const packId = match[1].toLowerCase();
  const packTitle = cleanText(body.pack_title, 120);
  const chapter = Number.isFinite(Number(body.chapter)) ? Number(body.chapter) : null;
  const chapterTitle = cleanText(body.chapter_title, 180);

  await env.DB.prepare(`
    INSERT INTO question_review_reports (
      question_id, pack_id, pack_title, chapter, chapter_title,
      first_reported_at, last_reported_at, report_count
    ) VALUES (?, ?, ?, ?, ?, ?, ?, 1)
    ON CONFLICT(question_id) DO UPDATE SET
      pack_id = excluded.pack_id,
      pack_title = CASE WHEN excluded.pack_title <> '' THEN excluded.pack_title ELSE question_review_reports.pack_title END,
      chapter = COALESCE(excluded.chapter, question_review_reports.chapter),
      chapter_title = CASE WHEN excluded.chapter_title <> '' THEN excluded.chapter_title ELSE question_review_reports.chapter_title END,
      last_reported_at = excluded.last_reported_at,
      report_count = question_review_reports.report_count + 1
  `).bind(
    questionId,
    packId,
    packTitle,
    chapter,
    chapterTitle,
    now,
    now,
  ).run();

  const row = await env.DB.prepare(`
    SELECT question_id, pack_id, pack_title, chapter, chapter_title,
           first_reported_at, last_reported_at, report_count
    FROM question_review_reports
    WHERE question_id = ?
  `).bind(questionId).first();

  return json({ status: row.report_count > 1 ? "already_submitted" : "submitted", report: row }, 200, cors);
}

async function listReports(env) {
  const result = await env.DB.prepare(`
    SELECT question_id, pack_id, pack_title, chapter, chapter_title,
           first_reported_at, last_reported_at, report_count
    FROM question_review_reports
    ORDER BY last_reported_at ASC
  `).all();
  return json({ reports: result.results || [] });
}

async function clearReport(questionId, env) {
  if (!PFQ_ID.test(questionId)) {
    return json({ error: "Invalid question ID" }, 400);
  }
  const result = await env.DB.prepare(
    "DELETE FROM question_review_reports WHERE question_id = ?"
  ).bind(questionId).run();
  return json({ cleared: questionId, deleted: Number(result.meta?.changes || 0) > 0 });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      const headers = corsHeaders(request, env);
      if (!headers["access-control-allow-origin"]) return new Response(null, { status: 403 });
      return new Response(null, { status: 204, headers });
    }

    if (request.method === "GET" && url.pathname === "/health") {
      return json({ status: "ok", service: "prepflow-question-review" });
    }

    if (request.method === "POST" && url.pathname === "/reports") {
      return submitReport(request, env);
    }

    if (url.pathname === "/admin/reports" && request.method === "GET") {
      if (!requireAdmin(request, env)) return json({ error: "Unauthorized" }, 401);
      return listReports(env);
    }

    if (url.pathname.startsWith("/admin/reports/") && request.method === "DELETE") {
      if (!requireAdmin(request, env)) return json({ error: "Unauthorized" }, 401);
      return clearReport(decodeURIComponent(url.pathname.slice("/admin/reports/".length)), env);
    }

    return json({ error: "Not found" }, 404);
  },
};
