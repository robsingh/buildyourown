#step1: Implementation

import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            if not content:
                print(f"The file is empty. Please verify the file before proceeding.")
                sys.exit(1)
        return content

    except FileNotFoundError:
        print(f"File not found.")


def sorting_printing(file_path):
    file_content = read_file(file_path)
    sorting_content = sorted(file_content)
    for element in sorting_content:
        print(element, end="")


def main():
    if len(sys.argv) != 2:
        print("Usage: <script> words.txt | head -n5")
        sys.exit(1)

    file_path = sys.argv[1]
    sorting_printing(file_path)


if __name__ == "__main__":
    main()

