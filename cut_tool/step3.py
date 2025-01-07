'''
Step 3: Implementation
'''
import sys
import csv
import argparse

def parse_field_list(field_list):
    '''
    Parse the field list from the -f option.
    Supports comma-separated or whitespace-separated values.
    Converts 1-based indices to 0-based indices.
    '''
    fields = []
    try:
        # split by comma or whitespace
        for part in field_list.replace(",", " ").split():
            fields.append(int(part)-1) # 1-based to 0-based indexing.
    except ValueError:
        print(f"Error: fields must be integers!")
        sys.exit(1)
    
    return fields

def read_file(file_path, fields, delimiter):
    try:
        with open(file_path, 'r') as file:
            file_reader = csv.reader(file, delimiter=delimiter)
            for row in file_reader:
                # extract the specified fields, substitute empty string if the field is missing
                selected_fields = [row[i] if i < len(row) else "" for i in fields]
                print(delimiter.join(selected_fields))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A custom implementation of the cut command.")
    parser.add_argument("-f", type=str, required=True, help="Comma or space-separated list of fields to extract (1-based indexing).")
    parser.add_argument("-d", type=str, default="\t", help="Delimiter to use (default:tab).")
    parser.add_argument("file", help="Path to input file.")
    args = parser.parse_args()

    # parse the field list and validate
    fields = parse_field_list(args.f)
    if any(field < 0 for field in fields):
        print("Error: Field indices must be 1 or greater.")
        sys.exit(1)

    read_file(args.file, fields, args.d)