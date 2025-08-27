# Marketing Attribution Warehouse

Think of this as a tiny marketing warehouse. It fabricates campaign spend and conversion events so you can explore dimensional modeling and ELT patterns in the cloud.

## Highlights

- Generates sample marketing spend and conversion events.
- Can stage the CSV to Amazon S3 or load directly into Google BigQuery.
- Calculates cost-per-acquisition (CPA) per campaign and writes a channel summary to `summary.csv`.
- Friendly starting point for conversations about star schemas and incremental loads.

## Run it

```bash
python src/ingest.py
```

You'll get a `marketing.csv` file with twenty rows. The environment resources below let you send the data to the cloud:

| Resource | Purpose |
|---------|---------|
| `S3_BUCKET` | S3 bucket for staging CSV |
| `BQ_TABLE` | BigQuery table destination |
| `ROWS` | Number of records to create (default: `20`) |
| `LOCAL_FILE` | Local CSV name (default: `marketing.csv`) |

If a dependency or credential is missing, the script just keeps everything local while still producing the `summary.csv`.
