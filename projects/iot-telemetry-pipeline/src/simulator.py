"""Simulate IoT device telemetry and publish to cloud."""

import json
import os
import random
import time
from datetime import datetime
from typing import Dict


def generate_event(device_id: int) -> Dict[str, object]:
    """Return a single telemetry event."""
    return {
        "device_id": device_id,
        "ts": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(15, 30), 2),
    }


def publish_kinesis(event: Dict[str, object], stream: str) -> None:
    """Send the event to an AWS Kinesis stream."""
    try:  # pragma: no cover - optional dependency
        import boto3

        client = boto3.client("kinesis")
        client.put_record(StreamName=stream, Data=json.dumps(event), PartitionKey=str(event["device_id"]))
        print(f"Published to Kinesis stream {stream}")
    except Exception as exc:
        print(f"Kinesis publish skipped: {exc}")


def publish_pubsub(event: Dict[str, object], topic: str) -> None:
    """Send the event to a GCP Pub/Sub topic."""
    try:  # pragma: no cover - optional dependency
        from google.cloud import pubsub_v1

        publisher = pubsub_v1.PublisherClient()
        publisher.publish(topic, json.dumps(event).encode("utf-8"))
        print(f"Published to Pub/Sub topic {topic}")
    except Exception as exc:
        print(f"Pub/Sub publish skipped: {exc}")


def main() -> None:
    rows = int(os.getenv("ROWS", "5"))
    out = os.getenv("LOCAL_FILE", "telemetry.jsonl")
    kinesis_stream = os.getenv("KINESIS_STREAM")
    pubsub_topic = os.getenv("PUBSUB_TOPIC")

    with open(out, "w") as fh:
        for i in range(rows):
            event = generate_event(device_id=i + 1)
            fh.write(json.dumps(event) + "\n")

            if kinesis_stream:
                publish_kinesis(event, kinesis_stream)
            if pubsub_topic:
                publish_pubsub(event, pubsub_topic)

            time.sleep(0.1)

    print(f"Wrote {rows} events to {out}")


if __name__ == "__main__":
    main()

