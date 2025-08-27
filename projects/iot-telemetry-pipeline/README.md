# IoT Telemetry Pipeline

A real-time data pipeline that streams synthetic IoT device metrics to both **AWS** and **Google Cloud Platform**. It highl
ights key skills from the data engineering roadmap including:

- **Stage 5 – Cloud Platforms:** demonstrates AWS Kinesis and Google Pub/Sub.
- **Stage 9 – Real-Time Pipelines:** simulates device telemetry streaming.
- **Stage 10 – CI/CD & DevOps:** script is container-friendly and easily integrated into workflows.

## Running locally

Generate a handful of telemetry events and write them to a JSON Lines file:

```bash
python src/simulator.py
```

Set the following optional environment variables to interact with cloud services:

| Variable | Purpose |
|---------|---------|
| `KINESIS_STREAM` | AWS Kinesis stream name for publishing events |
| `PUBSUB_TOPIC` | GCP Pub/Sub topic path for publishing events |
| `ROWS` | Number of events to generate (default: `5`) |
| `LOCAL_FILE` | Output file for JSON Lines (default: `telemetry.jsonl`) |

The script only requires Python's standard library for local execution. Cloud publishers are best-effort and safely skip whe
n dependencies or credentials are missing.

