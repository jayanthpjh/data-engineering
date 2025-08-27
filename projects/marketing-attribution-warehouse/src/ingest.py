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
        rows.append(
            {
                "campaign_id": i + 1,
                "ts": (start - timedelta(days=i)).date().isoformat(),
                "channel": random.choice(CHANNELS),
                "spend": round(random.uniform(100, 1000), 2),
                "impressions": random.randint(1000, 10000),
                "conversions": random.randint(0, 50),
            }
        )
    return rows


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


if __name__ == "__main__":
    main()

