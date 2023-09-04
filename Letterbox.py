class Letterbox:

    def __init__(self, owner):
        self.owner = owner
        self.has_letter = False

    def receive_letter(self, letter):
        self.has_letter = True

    def remove_letter(self):
        if self.has_letter:
            self.has_letter = False
            return True
        else:
            return False
