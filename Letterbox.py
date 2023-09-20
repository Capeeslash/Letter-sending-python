from Letter import Letter


class Letterbox:

    def __init__(self, owner):
        self.owner = owner
        self.has_letter = False
        self.received_letter = None

    def receive_letter(self, letter):
        self.has_letter = True
        self.received_letter = letter

    def remove_letter(self):
        if self.has_letter:
            self.has_letter = False
            return self.received_letter
        else:
            return None
