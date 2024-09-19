from typing import List
from conversation import Conversation
from message import Message

class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.conversations = []

    def create_conversation(self, user: 'User') -> Conversation:
        from conversation import Conversation
        conversation = Conversation([self, user])
        self.conversations.append(conversation)
        user.conversations.append(conversation)
        return conversation

    def send_message(self, message: Message, conversation: Conversation) -> None:
        if conversation in self.conversations:
            conversation.add_message(message)
            # Notify other participants (not implemented here)

    def receive_message(self, message: Message) -> None:
        if message.conversation in self.conversations:
            message.display_content()

    def manage_settings(self) -> None:
        # Settings management logic here
        pass

    def get_conversations(self) -> List[Conversation]:
        return self.conversations
