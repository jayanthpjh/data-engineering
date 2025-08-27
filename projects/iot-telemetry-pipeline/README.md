# IoT Telemetry Pipeline

Pretend you have a fleet of sensors pinging back temperature readings. This tiny project fakes those events so you can chat about streaming architectures without spinning up real hardware.

## Highlights

- Emits JSON Lines events to a local file for quick inspection.
- Can stream the same events to Amazon Kinesis or Google Pub/Sub when credentials are present.
- Pure Python and tiny—perfect for demos or coding exercises.
- Computes the average temperature and writes it to `summary.json`.

## Run it

```bash
python src/simulator.py
```

A file named `telemetry.jsonl` appears with five events. Tune the behaviour with environment resources:

| Resource | Purpose |
|---------|---------|
| `KINESIS_STREAM` | AWS Kinesis stream name |
| `PUBSUB_TOPIC` | GCP Pub/Sub topic path |
| `ROWS` | Number of events (default: `5`) |
| `LOCAL_FILE` | Output file name (default: `telemetry.jsonl`) |
| `SUMMARY_FILE` | Where to write the JSON summary (default: `summary.json`) |

Missing credentials or libraries? The script simply writes the events and summary to local files.
