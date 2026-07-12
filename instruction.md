Parse access log at `/app/access.log` and write a JSON summary report to `/app/report.json`.

Criteria to validate against:

1. `/app/report.json` exists and contains valid JSON.
2. `total_requests` equals the total number of request lines in `access.log`.
3. `unique_ips` equals the number of distinct client IP addresses.
4. `top_path` equals the request path.
