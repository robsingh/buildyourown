'''
Step 1: Use a tab separated file and print out the second field from each line.

If I want to alias this script to behave exactly like the 'cut' command, preferable way is to create the alias
in the shell configuration file.
'''
import sys
import csv
import argparse

def read_tsv_file(file_path, field_index):
    try:
        with open(file_path, 'r') as file:
            tsv_reader = csv.reader(file, delimiter='\t')
            empty = True
            for row in tsv_reader:
                empty = False
                if len(row) > field_index: # ensure the field exists
                    print(row[field_index])
                else:
                    print("")
            if empty:
                print("The file is empty!")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A custom implementation of the 'cut' command.")
    parser.add_argument("-f", type=int, required=True, help="Field index to extract (1-based indexing)")
    parser.add_argument("file", help="Path to the input TSV file.")
    args = parser.parse_args()

    # validate that -f is positive
    if args.f < 1:
        print(f"Error: Field index must be 1 or greater.")
        sys.exit(1)

    # convert the 1-based field index from '-f' to 0-based for Python
    field_index = args.f - 1

    read_tsv_file(args.file, field_index)