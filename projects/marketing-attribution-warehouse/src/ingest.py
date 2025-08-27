"""Generate marketing attribution data and optionally export to AWS/GCP."""

import csv
import os
import random
from datetime import datetime, timedelta
from typing import Dict, List

CHANNELS = ["search", "social", "email", "display"]


def generate_marketing_data(n: int = 20) -> List[Dict[str, object]]:
    """Return ``n`` rows of fake marketing spend/conversion data."""
    start = datetime.utcnow()
    rows: List[Dict[str, object]] = []
    for i in range(n):
        conversions = random.randint(0, 50)
        spend = round(random.uniform(100, 1000), 2)
        cpa = round(spend / conversions, 2) if conversions else None
        rows.append(
            {
                "campaign_id": i + 1,
                "ts": (start - timedelta(days=i)).date().isoformat(),
                "channel": random.choice(CHANNELS),
                "spend": spend,
                "impressions": random.randint(1000, 10000),
                "conversions": conversions,
                "cpa": cpa,
            }
        )
    return rows


def summarize_by_channel(rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    """Return aggregated spend/conversions per channel with CPA."""
    totals: Dict[str, Dict[str, float]] = {}
    for row in rows:
        channel = str(row["channel"])
        if channel not in totals:
            totals[channel] = {"spend": 0.0, "conversions": 0.0}
        totals[channel]["spend"] += float(row["spend"])
        totals[channel]["conversions"] += float(row["conversions"])
    summary: List[Dict[str, object]] = []
    for channel, vals in totals.items():
        conversions = vals["conversions"]
        cpa = round(vals["spend"] / conversions, 2) if conversions else None
        summary.append(
            {
                "channel": channel,
                "spend": round(vals["spend"], 2),
                "conversions": int(conversions),
                "cpa": cpa,
            }
        )
    return summary


def upload_to_s3(rows: List[Dict[str, object]], bucket: str, key: str) -> None:
    """Upload rows as CSV to S3."""
    try:  # pragma: no cover - optional dependency
        import boto3
        import io

        if not rows:
            raise ValueError("no data to upload")

        s3 = boto3.client("s3")
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
        s3.put_object(Bucket=bucket, Key=key, Body=buf.getvalue())
        print(f"Uploaded to s3://{bucket}/{key}")
    except Exception as exc:
        print(f"S3 upload skipped: {exc}")


def load_to_bigquery(rows: List[Dict[str, object]], table: str) -> None:
    """Load rows into BigQuery."""
    try:  # pragma: no cover - optional dependency
        from google.cloud import bigquery

        client = bigquery.Client()
        job = client.load_table_from_json(rows, table)
        job.result()
        print(f"Loaded {len(rows)} rows into BigQuery table {table}")
    except Exception as exc:
        print(f"BigQuery load skipped: {exc}")


def main() -> None:
    rows = int(os.getenv("ROWS", "20"))
    data = generate_marketing_data(rows)

    bucket = os.getenv("S3_BUCKET")
    key = os.getenv("S3_KEY", "marketing.csv")
    table = os.getenv("BQ_TABLE")

    if bucket:
        upload_to_s3(data, bucket, key)
    else:
        print("S3_BUCKET not set; skipping S3 upload.")

    if table:
        load_to_bigquery(data, table)
    else:
        print("BQ_TABLE not set; skipping BigQuery load.")

    out = os.getenv("LOCAL_FILE", "marketing.csv")
    if data:
        with open(out, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Wrote {len(data)} rows to {out}")

        summary = summarize_by_channel(data)
        with open("summary.csv", "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=["channel", "spend", "conversions", "cpa"])
            writer.writeheader()
            writer.writerows(summary)
        print("Wrote channel summary to summary.csv")


if __name__ == "__main__":
    main()

