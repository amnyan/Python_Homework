from typing import List
from user import User
from message import Message

class Conversation:
    def __init__(self, participants: List[User]):
        self.participants = participants
        self.message_history = []

    def add_message(self, message: Message):
        self.message_history.append(message)

    def add_user(self, user: User):
        if user not in self.participants:
            self.participants.append(user)

    def get_messages(self) -> List[Message]:
        return self.message_history
