# Marketing Attribution Warehouse

This project builds a tiny marketing data warehouse on **AWS** and **GCP**. It demonstrates:

- **Stage 1 – SQL & Database Fundamentals:** star schema with campaign and channel dimensions.
- **Stage 3 – Data Modeling & ELT/ETL:** Python script creates staging data ready for dbt or warehouse loads.
- **Stage 7 – Data Lakes & Warehouses:** data can be pushed to Amazon Redshift and Google BigQuery.

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

No external packages are required for local execution. Cloud steps are attempted only when dependencies and credentials are
available.

