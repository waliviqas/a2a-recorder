from recorder.message import Message
from recorder.sqlite_storage import SQLiteStorage
from recorder.adapters.crewai import CrewAIAdapter


class Recorder:
    @staticmethod
    def start(crew, path="recordings.db"):
        storage = SQLiteStorage(path)
        adapter = CrewAIAdapter(storage)
        adapter.wrap(crew)
        return adapter


__all__ = ["Message", "Recorder"]
