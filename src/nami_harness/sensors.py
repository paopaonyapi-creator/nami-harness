from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class SensorEvent:
    event_type: str
    payload: dict[str, Any]
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class JsonlSensor:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def record(self, event_type: str, payload: dict[str, Any]) -> SensorEvent:
        event = SensorEvent(event_type=event_type, payload=payload)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(asdict(event), ensure_ascii=False, sort_keys=True))
            file.write("\n")
        return event
