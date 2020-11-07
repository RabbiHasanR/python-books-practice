def show_messages(messages):
    """Show all messages is in list"""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Display all send message and add every message in new list"""
    while messages:
        current_message = messages.pop()

        print(f"Send successfully message: {current_message}")
        sent_messages.append(current_message)

def arrived_messages(sent_messages):
    """Display all arrived messages"""
    for sent_message in sent_messages:
        print(sent_message)

messages = ['hi', 'hello', 'rabbi', 'piash']
sent_messages = []

show_messages(messages)
send_messages(messages[:],sent_messages)
arrived_messages(sent_messages)



