# This challenge is to build your own JSON parser.
'''
Step 1: Implementation
Notes:
exit(1) means there was some issue/error/problem and that is why problem is exciting
exit(0) means clean exit without any errors/problems
'''

import sys
'''
# Lexer : Tokenize the input string
def lexer(json_string):
    tokens = []
    for char in json_string.strip():
        if char in '{}':
            tokens.append(char)
    return tokens

# Parser : Check if the tokens form a valid JSON object
def parser(tokens):
    # for this step, we are only validating an empty object '{}'
    if len(tokens) == 2 and tokens[0] == '{' and tokens[1] == '}':
        return True
    else:
        return False
    
# main function to handle input and output
def main():
    if len(sys.argv) != 2:
        print("Usage: json_parser <file>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            json_string = file.read()
        
        # Lex and parse the JSON string
        tokens = lexer(json_string)
        is_valid = parser(tokens)

        if is_valid:
            print("valid")
            sys.exit(0)
        else:
            print("invalid")
            sys.exit(1)
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''

