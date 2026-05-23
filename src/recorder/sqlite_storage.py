import sqlite3
import json
from pathlib import Path
from recorder.message import Message


class SQLiteStorage:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.path))
        self._create_table()

    def _create_table(self) -> None:
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                conversation_id TEXT NOT NULL,
                turn INTEGER NOT NULL,
                from_agent TEXT NOT NULL,
                to_agent TEXT NOT NULL,
                content TEXT NOT NULL,
                protocol TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def write(self, message: Message) -> None:
        data = message.to_dict()
        self.conn.execute(
            """INSERT INTO messages (id, conversation_id, turn, from_agent, to_agent, content, protocol, timestamp)
               VALUES (:id, :conversation_id, :turn, :from_agent, :to_agent, :content, :protocol, :timestamp)""",
            data,
        )
        self.conn.commit()
