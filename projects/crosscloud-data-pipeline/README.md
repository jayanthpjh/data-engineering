# Cross-Cloud Data Pipeline

Retail teams rarely live in a single cloud. This mini project shows how one tiny Python script can send the exact same dataset to both AWS and GCP without touching the business logic.

## Highlights

- Generates synthetic point‑of‑sale data with plain Python.
- Uploads the CSV to Amazon S3 or loads it straight into Google BigQuery when credentials are present.
- Computes store-level revenue totals and writes them to `summary.csv`.
- Optional Terraform module stands up the demo bucket and dataset.
- Dockerfile lets you run the pipeline in a clean container.

## Run it

```bash
python src/generator.py
```

By default a file named `output.csv` appears locally. Add environment resources to reach the cloud:

| Resource | Purpose |
|---------|---------|
| `S3_BUCKET` | S3 bucket to upload the CSV |
| `S3_KEY` | Object key in S3 (default: `sales.csv`) |
| `BQ_TABLE` | BigQuery table in `dataset.table` format |
| `ROWS` | Number of rows to create (default: `10`) |
| `LOCAL_FILE` | Name of the local CSV (default: `output.csv`) |

No credentials? The script simply keeps everything on disk and produces a `summary.csv` with revenue totals per store.

## Infrastructure

Terraform files in [`terraform`](terraform) create the S3 bucket and BigQuery dataset/table.

```bash
cd terraform
terraform init
terraform plan
```

Apply the plan and re-run the generator pointing at the new resources.

## Containers

Build the image to simulate a fresh environment:

```bash
docker build -t crosscloud-pipeline .
docker run --rm crosscloud-pipeline
```

## CI

A GitHub Actions workflow builds the container and runs the generator on every push.
