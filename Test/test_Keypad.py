import unittest
from Main.oldPhoneKeypad import numericToText

class TestNumericToText(unittest.TestCase):

    def test_valid_sequences(self):
        # Valid sequences that should decode correctly
        self.assertEqual(numericToText("22 777*#"), "B")
        self.assertEqual(numericToText("444 33*8#"), "IT")
        self.assertEqual(numericToText("2 33 8*4#"), "AEG")
        self.assertEqual(numericToText("7777*22#"), "B")
        self.assertEqual(numericToText("99*#"), "")

    def test_sequences_with_asterisk(self):
        # Sequences with asterisks to remove previous strokes
        self.assertEqual(numericToText("33 77777*#"), "E")
        self.assertEqual(numericToText("4444*2 33#"), "AE")

    def test_invalid_sequences(self):
        # Invalid sequences that are not part of the keymap
        self.assertEqual(numericToText("5555 666*#"), "Error: Invalid input sequence")
        self.assertEqual(numericToText("555 77777#"), "Error: Invalid input sequence")

    def test_missing_trailing_hash(self):
        # Input that does not end with a '#'
        self.assertEqual(numericToText("66666"), "Error: Input must end with '#'")
        self.assertEqual(numericToText("22 777*"), "Error: Input must end with '#'")
        self.assertEqual(numericToText("444 33"), "Error: Input must end with '#'")

    def test_invalid_characters(self):
        # Invalid characters in the input
        self.assertEqual(numericToText("22a#"), "Error: Invalid character in input")
        self.assertEqual(numericToText("44! 33#"), "Error: Invalid character in input")
        self.assertEqual(numericToText("5*6b#"), "Error: Invalid character in input")

    def test_single_digit_sequences(self):
        # Valid sequences with single digits
        self.assertEqual(numericToText("2#"), "A")
        self.assertEqual(numericToText("#"), "")
        self.assertEqual(numericToText("5 0#"), "J")
        self.assertEqual(numericToText("7*#"), "")  # '*' removes previous digit, result is empty


# Run the tests
if __name__ == '__main__':
    unittest.main()
