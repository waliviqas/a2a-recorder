import json
from pathlib import Path
from recorder.message import Message


class JSONLStorage:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, message: Message) -> None:
        with self.path.open("a") as f:
            f.write(json.dumps(message.to_dict()) + "\n")
