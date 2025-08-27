# IoT Telemetry Pipeline


## Running locally



```bash
python src/simulator.py
```



| Resource | Purpose |
|---------|---------|
| `KINESIS_STREAM` | AWS Kinesis stream name for publishing events |
| `PUBSUB_TOPIC` | GCP Pub/Sub topic path for publishing events |
| `ROWS` | Number of events to generate (default: `5`) |
| `LOCAL_FILE` | Output file for JSON Lines (default: `telemetry.jsonl`) |



