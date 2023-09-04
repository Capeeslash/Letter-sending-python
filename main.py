import unittest
from People import People
from Letter import Letter
from Letterbox import Letterbox


class TestLetterSystem(unittest.TestCase):
    def setUp(self):
        self.alice = People("Alice", "123 Fake St")
        self.bob = People("Bob", "742 Evergreen Tce")
        self.bob_letterbox = Letterbox(self.bob)
        self.alice_letterbox = Letterbox(self.alice)

    def test_alice_writes_and_delivers_letter(self):
        letter = self.alice.write_letter(self.bob, "Howdy Bob")
        self.alice.send_letter(letter, self.bob_letterbox)
        self.assertTrue(self.bob_letterbox.has_letter)

    def test_alice_sends_two_letters_in_a_row(self):
        letter1 = self.alice.write_letter(self.bob, "Hello Hello")
        letter2 = self.alice.write_letter(self.bob, "Hello again!")
        self.alice.send_letter(letter1, self.bob_letterbox)
        result = self.alice.send_letter(letter2, self.bob_letterbox)
        self.assertIsNone(result)

 #   def test_bob_sends_letter_and_checks_if_read(self):

   # def test_alice_writes_and_bob_replies(self):

   # def test_bob_checks_letterbox_after_reading(self):



# if __name__ == '_main__':
    ##unittest.main()