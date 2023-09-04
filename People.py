from Letter import Letter
from Letterbox import Letterbox


class People:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.received_letter = False

    def write_letter(self, recipient, content):
        letter = Letter(self, recipient, content)
        return letter

    def check_letterbox(self, letterbox):
        if letterbox.has_letter:
            self.received_letter = True
            return letterbox.remove_letter()
        else:
            return None

    @staticmethod
    def read_letter(letter):
        letter.mark_as_read()
