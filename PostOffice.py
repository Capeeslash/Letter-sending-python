class PostOffice:
    def __init__(self):
        self.packages = []

    def receive_package(self, letter):
        self.packages.append(letter)

    def get_packages(self):
        return self.packages

    def clear_packages(self):
        self.packages = []

    def remove_letter(self):
        if self.packages:
            return self.packages.pop(0)
        else:
            return None
