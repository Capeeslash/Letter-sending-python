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
        self.post_office = PostOffice()
        self.charli = Charli(self.post_office)
        self.shift = 3

    def test_alice_writes_and_delivers_letter(self):
        letter = self.alice.write_letter(self.bob, "Howdy Bob")
        self.alice.send_letter(letter, self.post_office)
        self.charli.pickup_package()
        self.charli.deliver_letter()
        bob_letterbox = self.bob.letterbox
        self.assertTrue(bob_letterbox.has_letter)
        received_letter = bob_letterbox.remove_letter()
        self.assertIsNotNone(received_letter)
        self.assertEqual(received_letter.content, "Howdy Bob")

    def test_alice_sends_two_letters_in_a_row(self):
        letter1 = self.alice.write_letter(self.bob, "Hello Hello")
        letter2 = self.alice.write_letter(self.bob, "Hello again!")
        self.alice.send_letter(letter1, self.post_office)
        result = self.alice.send_letter(letter2, self.post_office)
        self.assertIsNone(result)

    def test_bob_sends_letter_and_checks_if_read(self):
        letter = self.bob.write_letter(self.alice, "Howdy friend!")
        self.bob.send_letter(letter, self.post_office)
        self.charli.pickup_package()
        self.charli.deliver_letter()
        received_letter = self.alice.letterbox.remove_letter()
        self.alice.read_letter(letter)
        self.assertTrue(letter.is_read)

    def test_alice_writes_and_bob_replies(self):
        letter1 = self.alice.write_letter(self.bob, "Hello, how are you?")
        self.alice.send_letter(letter1, self.post_office)
        self.charli.pickup_package()
        self.charli.deliver_letter()
        received_letter1 = self.bob.letterbox.remove_letter()
        self.assertIsNotNone(received_letter1)
        letter2 = self.bob.write_letter(self.alice, "I'm good, how are you?")
        self.bob.send_letter(letter2, self.post_office)
        self.charli.pickup_package()
        self.charli.deliver_letter()
        received_letter2 = self.alice.letterbox.remove_letter()
        self.assertIsNotNone(received_letter2)
        self.assertEqual(received_letter2.content, "I'm good, how are you?")

    def test_bob_writes_alice_encrypted_letter(self):
        bob_letter = self.bob.write_letter(self.alice, "Hi Alice, just testing our new secret code!")
        self.bob.encrypt_letter(bob_letter, self.shift)
        self.bob.send_letter(bob_letter, self.post_office)
        self.charli.pickup_package()
        self.charli.deliver_letter()
        alice_received_letter = self.alice.letterbox.remove_letter()
        print(f"Encrypted Letter Content: {alice_received_letter.content}")
        self.assertIsNotNone(alice_received_letter)
        self.assertFalse(alice_received_letter.is_read)
        self.alice.decrypt_letter(alice_received_letter, self.shift)
        self.assertEqual(alice_received_letter.content, "Hi Alice, just testing our new secret code!")
