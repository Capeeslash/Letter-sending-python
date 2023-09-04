class Letter:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True
