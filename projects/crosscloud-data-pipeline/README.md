# Cross-Cloud Data Pipeline

This project demonstrates a minimal data pipeline that can operate across **AWS** and **Google Cloud Platform**. It
creates synthetic sales data, optionally uploads the dataset to an Amazon S3 bucket, and can load the same data into a
BigQuery table.

The code is intended as a small but complete example you can extend for real-world use or showcase during interviews.

## Requirements

- Python 3.11+
- (Optional) `boto3` and `google-cloud-bigquery` for cloud uploads
- (Optional) AWS credentials configured via environment variables or shared credentials file
- (Optional) GCP credentials configured for the `google-cloud-bigquery` client

## Running locally

Execute the generator with Python:

```bash
python src/generator.py
```

The script will generate a CSV file `output.csv` in the project directory. Install the optional requirements and provide the following environment variables to interact with cloud services:

| Variable | Purpose |
|---------|---------|
| `S3_BUCKET` | Name of the destination S3 bucket |
| `S3_KEY` | Object key for the uploaded CSV (default: `sales.csv`) |
| `BQ_TABLE` | BigQuery destination table in the form `dataset.table` |
| `ROWS` | Number of synthetic rows to generate (default: `10`) |
| `LOCAL_FILE` | Local filename for the generated CSV (default: `output.csv`) |

When any of these services are not configured or credentials are missing, the script safely skips that step and
continues.

## Docker

A `Dockerfile` is provided to guarantee reproducible environments. Build and run:

```bash
docker build -t crosscloud-pipeline .
docker run --rm crosscloud-pipeline
```

This container executes the same `generator.py` script, allowing you to verify that the project builds on a clean system
such as CI runners or another developer's machine.

## CI

A GitHub Actions workflow in `.github/workflows/ci.yml` installs dependencies and runs the generator inside Docker to
validate the project on every push.
