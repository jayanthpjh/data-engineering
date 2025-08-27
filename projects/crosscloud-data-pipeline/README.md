# Cross-Cloud Data Pipeline


## Running locally

Execute the generator with Python:

```bash
python src/generator.py
```


| Resource | Purpose |
|---------|---------|
| `S3_BUCKET` | Name of the destination S3 bucket |
| `S3_KEY` | Object key for the uploaded CSV (default: `sales.csv`) |
| `BQ_TABLE` | BigQuery destination table in the form `dataset.table` |
| `ROWS` | Number of synthetic rows to generate (default: `10`) |
| `LOCAL_FILE` | Local filename for the generated CSV (default: `output.csv`) |



## Docker



```bash
docker build -t crosscloud-pipeline .
docker run --rm crosscloud-pipeline
```



## CI

A GitHub Actions workflow in `.github/workflows/ci.yml` installs dependencies and runs the generator inside Docker to
validate the project on every push.
