# PrepFlow question review service

Tiny Cloudflare Worker + D1 mailbox for the public **Send for review** button.

## Deploy

1. From `review-service/`, create the D1 database:
   `npx wrangler d1 create prepflow-question-review`
2. Put the returned database ID into `wrangler.toml`.
3. Apply the schema:
   `npx wrangler d1 execute prepflow-question-review --remote --file=schema.sql`
4. Create a long random admin token and store it as a Worker secret:
   `npx wrangler secret put ADMIN_TOKEN`
5. Deploy:
   `npx wrangler deploy`
6. Put the deployed Worker URL into `web/review-service-config.js`.
7. In the private Workbench environment set:
   - `PREPFLOW_REVIEW_SERVICE_URL=<worker-url>`
   - `PREPFLOW_REVIEW_ADMIN_TOKEN=<same admin token>`

The public browser never receives `ADMIN_TOKEN`. Public submissions are deduplicated by stable PFQ ID; repeated clicks increment `report_count` on the same queue row.
