'''
Step 4: Implementation
'''
import sys
import csv
import argparse

def parse_field_list(field_list):
    """
    Parse the field list from the -f option.
    Supports comma separated or whitespace separated values.
    Converts 1-based indices to 0-based indices.
    """
    fields = []
    try:
        for part in field_list.replace(",", " ").split():
            fields.append(int(part)-1)
    except ValueError:
        print(f"Error: fields must be integers.")
        sys.exit(1)
    
    return fields


def read_input(input_stream, fields, delimiter):
    """
    Read from the input stream (file or stdin), extract specified fields.
    """
    file_reader = csv.reader(input_stream, delimiter=delimiter)
    for row in file_reader:
        # extract the specified fields, substitute empty string if field is missing
        selected_fields = [row[i] if i < len(row) else "" for i in fields]
        print(delimiter.join(selected_fields))


def main():
    parser = argparse.ArgumentParser(description="A custom implementation of the 'cut' command.")
    parser.add_argument("-f", type=str, required=True, help="Comma or space-separated list of fields to extract (1-based indexing.)")
    parser.add_argument("-d", type=str, default="\t", help="Delimiter to use (default:tab).")
    parser.add_argument("file", nargs="?", default="-", help="Path to the input file or '-' for standard input.")
    args = parser.parse_args()

    # parse the field list and validate
    fields = parse_field_list(args.f)
    if any(field < 0 for field in fields):
        print(f"Error:Field indices must be 1 or greater.")
        sys.exit(1)
    
    # determine input source (file or stdin)
    if args.file == "-":
        read_input(sys.stdin, fields, args.d)
    else:
        # read from file
        try:
            with open(args.file, 'r') as file:
                read_input(file, fields, args.d)
        except FileNotFoundError:
            print(f"File not found: {args.file}")
            sys.exit(1)

if __name__ == "__main__":
    main()