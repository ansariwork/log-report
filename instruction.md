Provided access log at `/app/access.log`.

Analyse the log and produce a JSON report at `/app/out.json` containing exactly
these three fields:

| Field            | Type    | Meaning                                        |
|------------------|---------|------------------------------------------------|
| `total_requests` | integer | Total number of log lines (requests)           |
| `unique_ips`     | integer | Number of distinct client IP addresses         |
| `top_path`       | string  | The URL path that appears most often in the log |

## Success criteria

1. The file `/app/out.json` exists and contains valid JSON.
2. `total_requests` is the exact count of log entries in the file.
3. `unique_ips` is the exact count of distinct IP addresses that made requests.
4. `top_path` is the URL path (e.g. `/index.html`) with the highest request count.

## Example output format

```json
{
  "total_requests": 42,
  "unique_ips": 7,
  "top_path": "/index.html"
}
```

No other keys are required. Whitespace and key order do not matter.
