import json
import tempfile
from pathlib import Path
from dataclasses import dataclass

from recorder.storage import JSONLStorage
from recorder.adapters.crewai import CrewAIAdapter


@dataclass
class FakeTaskOutput:
    agent: str
    raw: str


class FakeCrew:
    task_callback = None


def test_adapter_records_task_output():
    with tempfile.TemporaryDirectory() as tmp:
        recording_path = Path(tmp) / "out.jsonl"
        storage = JSONLStorage(recording_path)
        adapter = CrewAIAdapter(storage)

        crew = FakeCrew()
        adapter.wrap(crew)

        crew.task_callback(FakeTaskOutput(agent="researcher", raw="found 3 sources"))
        crew.task_callback(FakeTaskOutput(agent="writer", raw="drafted intro"))

        lines = recording_path.read_text().strip().split("\n")
        assert len(lines) == 2

        first = json.loads(lines[0])
        assert first["from_agent"] == "researcher"
        assert first["content"] == "found 3 sources"
        assert first["protocol"] == "crewai"
        assert first["turn"] == 1

        second = json.loads(lines[1])
        assert second["from_agent"] == "writer"
        assert second["turn"] == 2
        assert first["conversation_id"] == second["conversation_id"]

        print("PASS: 2 messages recorded, same conversation_id, turns 1 and 2")


if __name__ == "__main__":
    test_adapter_records_task_output()
