import unittest
from translator import french_to_english, english_to_french


class Test_translator(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english(None), "No string has been entered")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_english_to_french(self):
        self.assertEqual(english_to_french(None), "No string has been entered")
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        self.assertEqual(english_to_french("Hello"), "Bonjour")


if __name__ == "__main__":
    unittest.main()