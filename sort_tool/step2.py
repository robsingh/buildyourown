#step2: Implementation

import sys

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            if not content:
                print(f"The file is empty. Please verify the file.")
                sys.exit(1)
        return content

    except FileNotFoundError:
        print(f"File not found. Please try again.")


def sorting_unique(file_path):
    file_content = read_file(file_path)
    sorting = sorted(set(file_content))
    for element in sorting:
        print(element, end="")


def only_sorting(file_path):
    file_content = read_file(file_path)
    sorting_only = sorted(file_content)
    for element in sorting_only:
        print(element, end="")


def main():
    if len(sys.argv) == 2:
        # no -u flag, just sort
        file_path = sys.argv[1]
        use_unique = False
        only_sorting(file_path)

    elif len(sys.argv) == 3 and sys.argv[1] == "-u":
        #-u flag present
        file_path = sys.argv[2]
        use_unique = True
        sorting_unique(file_path)

    else:
        # wrong usage
        print("Usage: script.py [-u] filename")
    

if __name__ == "__main__":
    main()