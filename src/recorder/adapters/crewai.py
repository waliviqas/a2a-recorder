import uuid
from recorder.message import Message
from recorder.storage import JSONLStorage


class CrewAIAdapter:
    def __init__(self, storage: JSONLStorage):
        self.storage = storage
        self.conversation_id = str(uuid.uuid4())
        self.turn = 0

    def wrap(self, crew):
        original_callback = getattr(crew, "task_callback", None)

        def callback(task_output):
            self.turn += 1
            agent_name = getattr(task_output, "agent", "unknown")
            content = getattr(task_output, "raw", str(task_output))

            message = Message(
                conversation_id=self.conversation_id,
                from_agent=str(agent_name),
                to_agent="crew",
                content=str(content),
                protocol="crewai",
                turn=self.turn,
            )
            self.storage.write(message)

            if original_callback:
                return original_callback(task_output)

        crew.task_callback = callback
        return crew
