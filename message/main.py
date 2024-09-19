from datetime import datetime
from user import User
from conversation import Conversation
from textmessage import TextMessage
from multimediamessage import MultimediaMessage

def main():
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")

    # Create a conversation between Alice and Bob
    conv = user1.create_conversation(user2)

    # Send a text message
    msg1 = TextMessage(sender=user1, conversation=conv, timestamp=datetime.now(), content="Hello, Bob!")
    user1.send_message(msg1, conv)

    # Send a multimedia message
    msg2 = MultimediaMessage(sender=user2, conversation=conv, timestamp=datetime.now(), file_path="/path/to/image.jpg", media_type="Image")
    user2.send_message(msg2, conv)

    # Users receive messages
    user1.receive_message(msg2)
    user2.receive_message(msg1)

    # View conversation history
    for msg in conv.get_messages():
        msg.display_content()

if __name__ == "__main__":
    main()
