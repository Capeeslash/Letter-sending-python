from Letter import Letter
from Letterbox import Letterbox


class People:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.received_letter = False
        self.letterbox = Letterbox(self)

    def write_letter(self, recipient, content):
        letter = Letter(self, recipient, content)
        return letter

    def send_letter(self, letter, post_office):
        received_letter = self.check_letterbox(post_office)
        if not received_letter:
            post_office.receive_package(letter)  # Send the letter to the post office
            self.received_letter = False
        else:
            return None

    def check_letterbox(self, letterbox):
        received_letter = letterbox.remove_letter()
        if received_letter:
            self.received_letter = True
        return received_letter

    def encrypt_letter(self, letter, shift):
        if not letter.is_encrypted:
            encrypted_content = ""
            for char in letter.content:
                if char.isalpha():
                    shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord(
                        'a' if char.islower() else 'A'))
                    encrypted_content += shifted_char
                else:
                    encrypted_content += char
            letter.content = encrypted_content
            letter.is_encrypted = True

    def decrypt_letter(self, letter, shift):
        if letter.is_encrypted:
            decrypted_content = ""
            for char in letter.content:
                if char.isalpha():
                    shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26) + ord(
                        'a' if char.islower() else 'A'))
                    decrypted_content += shifted_char
                else:
                    decrypted_content += char
            letter.content = decrypted_content
            letter.is_encrypted = False

    @staticmethod
    def read_letter(letter):
        letter.mark_as_read()
