import sqlite3
import tempfile
from pathlib import Path

from recorder.message import Message
from recorder.sqlite_storage import SQLiteStorage


def test_sqlite_stores_and_reads():
    with tempfile.TemporaryDirectory() as tmp:
        db_path = Path(tmp) / "test.db"
        storage = SQLiteStorage(db_path)

        storage.write(Message(
            conversation_id="abc",
            from_agent="recruiter",
            to_agent="manager",
            content="Alice is a strong match",
            protocol="crewai",
            turn=1,
        ))
        storage.write(Message(
            conversation_id="abc",
            from_agent="manager",
            to_agent="recruiter",
            content="Why reject Bob?",
            protocol="crewai",
            turn=2,
        ))

        conn = sqlite3.connect(str(db_path))
        rows = conn.execute("SELECT from_agent, content, turn FROM messages ORDER BY turn").fetchall()

        assert len(rows) == 2
        assert rows[0] == ("recruiter", "Alice is a strong match", 1)
        assert rows[1] == ("manager", "Why reject Bob?", 2)

        print("PASS: 2 messages stored in SQLite, readable with standard SQL")


if __name__ == "__main__":
    test_sqlite_stores_and_reads()
