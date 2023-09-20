import unittest
from People import People
from Letter import Letter
from Letterbox import Letterbox
from PostOffice import PostOffice
from Charli import Charli


class TestLetterSystem(unittest.TestCase):
    def setUp(self):
        self.alice = People("Alice", "123 Fake St")
        self.bob = People("Bob", "742 Evergreen Tce")
        self.bob_letterbox = Letterbox(self.bob)
        self.alice_letterbox = Letterbox(self.alice)
        self.charli = Charli(PostOffice())

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

    def test_bob_sends_letter_and_checks_if_read(self):
        letter = self.bob.write_letter(self.alice, "Howdy friend!")
        self.bob.send_letter(letter, self.alice_letterbox)
        self.alice.check_letterbox(self.alice_letterbox)
        self.alice.read_letter(letter)
        self.assertTrue(letter.is_read)

    def test_alice_writes_and_bob_replies(self):
        letter1 = self.alice.write_letter(self.bob, "Hello, how are you?")
        self.alice.send_letter(letter1, self.bob_letterbox)
        received_letter1 = self.bob.check_letterbox(self.bob_letterbox)
        self.assertIsNotNone(received_letter1)
        letter2 = self.bob.write_letter(self.alice, "I'm good, how are you?")
        self.bob.send_letter(letter2, self.alice_letterbox)
        received_letter2 = self.alice.check_letterbox(self.alice_letterbox)
        self.assertIsNotNone(received_letter2)
        self.assertEqual(received_letter2.content, "I'm good, how are you?")
