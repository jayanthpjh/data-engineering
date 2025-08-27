# Marketing Attribution Warehouse


## Running locally

Generate synthetic ad spend and conversion records:

```bash
python src/ingest.py
```

Optional environment variables enable cloud uploads:

| Variable | Purpose |
|---------|---------|
| `S3_BUCKET` | S3 bucket for staging CSV |
| `BQ_TABLE` | BigQuery table for loading data |
| `ROWS` | Number of records to create (default: `20`) |
| `LOCAL_FILE` | Local CSV output (default: `marketing.csv`) |



