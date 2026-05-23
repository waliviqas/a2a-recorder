from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
import uuid


@dataclass
class Message:
    conversation_id: str
    from_agent: str
    to_agent: str
    content: str
    protocol: str
    turn: int = 0
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)
