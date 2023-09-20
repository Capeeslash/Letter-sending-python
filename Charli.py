from Letter import Letter


class Charli:
    def __init__(self, post_office):
        self.post_office = post_office
        self.has_package = False
        self.package = None

    def pickup_package(self):
        if not self.has_package:
            packages = self.post_office.get_packages()
            if packages:
                self.package = packages[0]
                self.has_package = True

    def deliver_letter(self):
        if self.has_package:
            recipient = self.package.recipient
            recipient.receive_letter(self.package)
            self.has_package = False
            self.post_office.clear_packages()
