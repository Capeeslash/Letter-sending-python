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

    def send_letter(self, letter, letterbox):
        received_letter = self.check_letterbox(letterbox)
        if not received_letter:
            letterbox.receive_letter(letter)
            self.received_letter = False
        else:
            return None

    def check_letterbox(self, letterbox):
        received_letter = letterbox.remove_letter()
        if received_letter:
            self.received_letter = True
        return received_letter

    @staticmethod
    def read_letter(letter):
        letter.mark_as_read()
