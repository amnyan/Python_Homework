from message import Message
from datetime import datetime
from user import User
from conversation import Conversation

class TextMessage(Message):
    def __init__(self, sender: User, conversation: Conversation, timestamp: datetime, content: str):
        super().__init__(sender, conversation, timestamp)
        self.content = content

    def display_content(self):
        print(f"Text Message from {self.sender.name}: {self.content}")

    def get_message_type(self) -> str:
        return "Text"
