# This challenge is to build your own JSON parser.

import sys
import re

'''
Step 1: Implementation
Notes:
exit(1) means there was some issue/error/problem and that is why problem is exciting
exit(0) means clean exit without any errors/problems
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
Step 2: Implementation
'''

def lexer(json_string):
    tokens = []
    json_string = json_string.strip()

    # regular expressions to match strings and other tokens
    string_pattern = r'"(.*?)"' # match anything inside double quotes
    other_pattern = r'[\{\}\:\,]' # match braces, colons, and commas

    # tokenizing the input
    index = 0
    while index < len(json_string):
        # match strings
        if json_string[index] == '"':
            match = re.match(string_pattern, json_string[index:])
            if match:
                tokens.append(match.group(0))
                index += len(match.group(0))
            else:
                return None # invalid string
        
        # match braces, colons, and commas
        elif json_string[index] in '{}:,':
            tokens.append(json_string[index])
            index += 1
        
        #skip spaces
        elif json_string[index].isspace():
            index += 1
        else:
            return None # invalid character
    
    return tokens

# Parser : Check if the tokens form a valid JSON object with string keys and values
def parser(tokens):
    if len(tokens) != 5:
        return False
    
    if (tokens[0] == '{' and tokens[1].startswith('"') and tokens[1].endswith('"') and
        tokens[2] == ':' and
        tokens[3].startswith('"') and tokens[3].endswith('"') and
        tokens[4] == '}'):
        return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: json_parser <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as file:
            json_string = file.read()
        
        # lex and parse the JSON string
        tokens = lexer(json_string)
        if tokens is None:
            print("invalid")
            sys.exit(1)
        
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