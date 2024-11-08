'''
Step 1: Implementation
'''
from collections import Counter
import os
import sys

def count_character_frequencies(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist or cannot be read.")
    frequencies = Counter()

    # read the file and update the frequency counter
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        frequencies.update(text)
    return dict(frequencies)


def main():
    if len(sys.argv) != 2:
        print("Usage: script_name.py <filename>")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        try:
            frequency_table = count_character_frequencies(filename)
            print(frequency_table)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
            

if __name__ == "__main__":
    main()

