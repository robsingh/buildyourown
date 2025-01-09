'''
Step 5: Implementation
'''
import csv
import sys
import argparse

def parse_field_list(field_list):
    fields = []
    try:
        for part in field_list.replace(",", " ").split():
            fields.append(int(part)-1)
    except ValueError:
        print(f"Error: fields must be integers.")
        sys.exit(1)

    return fields


def read_input(input_stream, fields, delimiter, unique=False, count=False):
    file_reader = csv.reader(input_stream, delimiter=delimiter)
    results = []

    for row in file_reader:
        selected_fields = [row[i] if i < len(row) else "" for i in fields]
        results.append(delimiter.join(selected_fields))

    if unique:
        results = sorted(set(results))
    
    if count:
        print(len(results))
    else:
        for line in results:
            print(line)


def main():
    parser = argparse.ArgumentParser(description="A custom implementation of the 'cut' command.")
    parser.add_argument("-f", type=str, required=True, help="Commna or space-separated list of fields to extract (1-based indexing).")
    parser.add_argument("-d", type=str, default="\t", help="Delimiter to use (default:tab).")
    parser.add_argument("--unique", action="store_true", help="Only Output unique lines.")
    parser.add_argument("--count", action="store_true", help="Count the number of unique lines.")
    parser.add_argument("file", nargs="?", default="-", help="Path to the input file or '-' for the standard input.")
    args = parser.parse_args()

    fields = parse_field_list(args.f)
    if any(field < 0 for field in fields):
        print(f"Error: Field indices must be 1 or greater.")
        sys.exit(1)

    
    if args.file == "-":
        read_input(sys.stdin, fields, args.d, unique=args.unique, count=args.count)
    else:
        try:
            with open(args.file, 'r') as file:
                read_input(file, fields, args.d, unique=args.unique, count=args.count)
        except FileNotFoundError:
            print(f"File not found: {args.file}")
            sys.exit(1)


if __name__ == "__main__":
    main()