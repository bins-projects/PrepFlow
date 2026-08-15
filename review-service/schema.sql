CREATE TABLE IF NOT EXISTS question_review_reports (
  question_id TEXT PRIMARY KEY,
  pack_id TEXT NOT NULL,
  pack_title TEXT NOT NULL DEFAULT '',
  chapter INTEGER,
  chapter_title TEXT NOT NULL DEFAULT '',
  first_reported_at TEXT NOT NULL,
  last_reported_at TEXT NOT NULL,
  report_count INTEGER NOT NULL DEFAULT 1 CHECK (report_count >= 1)
);

CREATE INDEX IF NOT EXISTS question_review_reports_last_reported_at
  ON question_review_reports(last_reported_at);
