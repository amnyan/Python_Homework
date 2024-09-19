from abc import ABC, abstractmethod
from datetime import datetime
from user import User
from conversation import Conversation

class Message(ABC):
    def __init__(self, sender: User, conversation: Conversation, timestamp: datetime):
        self.sender = sender
        self.conversation = conversation
        self.timestamp = timestamp

    @abstractmethod
    def display_content(self):
        pass

    @abstractmethod
    def get_message_type(self) -> str:
        pass
