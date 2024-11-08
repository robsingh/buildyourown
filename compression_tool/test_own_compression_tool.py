from own_compression_tool import count_character_frequencies
import unittest
import os

class TestCharacterFrequencies(unittest.TestCase):
    def test_count_character_frequencies(self):
        # sample text
        sample_text = "Hello, World!"

        temp_filename = "sample_text.txt"
        with open(temp_filename, "w") as f:
            f.write(sample_text)

        # expected frequency table
        expected_output = {
            'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1,
            'W': 1, 'r': 1, 'd': 1, '!': 1
        }

        # call the function and verify the output
        result = count_character_frequencies(temp_filename)
        self.assertEqual(result, expected_output)

        # cleanup the temp file
        os.remove(temp_filename)


if __name__ == "__main__":
    unittest.main()