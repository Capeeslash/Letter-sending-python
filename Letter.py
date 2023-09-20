class Letter:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.is_read = False
        self.is_encrypted = False

    def mark_as_read(self):
        self.is_read = True

    def encrypt_letter(self, shift):
        if not self.is_encrypted:
            encrypted_content = ""
            for char in self.content:
                if char.isalpha():
                    shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord(
                        'a' if char.islower() else 'A'))
                    encrypted_content += shifted_char
                else:
                    encrypted_content += char
            self.content = encrypted_content
            self.is_encrypted = True

    def decrypt_letter(self, shift):
        if self.is_encrypted:
            decrypted_content = ""
            for char in self.content:
                if char.isalpha():
                    shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26) + ord(
                        'a' if char.islower() else 'A'))
                    decrypted_content += shifted_char
                else:
                    decrypted_content += char
            self.content = decrypted_content
            self.is_encrypted = False
