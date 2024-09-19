from message import Message
from datetime import datetime
from user import User
from conversation import Conversation

class MultimediaMessage(Message):
    def __init__(self, sender: User, conversation: Conversation, timestamp: datetime, file_path: str, media_type: str):
        super().__init__(sender, conversation, timestamp)
        self.file_path = file_path
        self.media_type = media_type

    def display_content(self):
        print(f"{self.media_type} Message from {self.sender.name}: {self.file_path}")

    def get_message_type(self) -> str:
        return self.media_type
