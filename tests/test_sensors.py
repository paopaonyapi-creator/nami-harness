import json

from nami_harness.sensors import JsonlSensor


def test_jsonl_sensor_records_event(tmp_path) -> None:
    path = tmp_path / "events.jsonl"
    sensor = JsonlSensor(path)

    event = sensor.record("task.completed", {"agent": "hermes"})

    line = path.read_text(encoding="utf-8").strip()
    record = json.loads(line)
    assert record["event_id"] == event.event_id
    assert record["event_type"] == "task.completed"
    assert record["payload"] == {"agent": "hermes"}
