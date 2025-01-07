'''
Step 2 : Implementation
'''
import csv
import argparse
import sys

def read_file(file_path, field_index, delimiter):
    try:
        with open(file_path, 'r') as file:
            file_reader = csv.reader(file, delimiter=delimiter)
            empty = True
            for row in file_reader:
                empty = False
                if len(row) > field_index:
                    print(row[field_index])
                else:
                    print("")
            if empty:
                print(f"The file is empty!")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A custom implementation of the 'cut' command.")
    parser.add_argument("-f", type=int, required=True, help="Field index to extract (1-based indexing).")
    parser.add_argument("-d", type=str, default="\t", help="Delimiter to use (default: tab).")
    parser.add_argument("file", help="Path to the input CSV/TSV file.")
    args = parser.parse_args()

    if args.f < 1:
        print("Error: Field index must be 1 or greater.")
        sys.exit(1)

    field_index = args.f - 1
    read_file(args.file, field_index, args.d)