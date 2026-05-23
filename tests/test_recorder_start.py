import sqlite3
import tempfile
from pathlib import Path
from dataclasses import dataclass

from recorder import Recorder


@dataclass
class FakeTaskOutput:
    agent: str
    raw: str


class FakeCrew:
    task_callback = None


def test_recorder_start():
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "test.db"
        crew = FakeCrew()
        Recorder.start(crew, path=str(db_path))

        crew.task_callback(FakeTaskOutput(agent="recruiter", raw="Alice is strong"))
        crew.task_callback(FakeTaskOutput(agent="manager", raw="Why reject Bob?"))

        conn = sqlite3.connect(str(db_path))
        rows = conn.execute("SELECT from_agent, content, turn FROM messages ORDER BY turn").fetchall()

        assert len(rows) == 2
        assert rows[0] == ("recruiter", "Alice is strong", 1)
        assert rows[1] == ("manager", "Why reject Bob?", 2)

        print("PASS: Recorder.start() works — one line, SQLite, 2 messages recorded")


if __name__ == "__main__":
    test_recorder_start()
