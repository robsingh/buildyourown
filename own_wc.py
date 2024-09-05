'''
Build your own version of Unix command line tool 'wc'.
wc - word, line, character, and byte count. 
'''
'''
Step 1:
Simple version of wc. Let's call it ccwc that takes the command line option -c and outputs number of bytes in a file.

ccwc -c test.txt
'''

import os
import sys

def ccwc():
    if len(sys.argv) != 3:
        print("Usage: ccwc -c <filename>")
        return 
    
    option, filename = sys.argv[1], sys.argv[2]

    if option != '-c':
        print(f"Unknown option: {option}")
        return
    
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
    
    try:
        with open(filename, 'rb') as file:
            read_data = file.read()
        num_bytes = len(read_data)
        print(num_bytes)
    except FileNotFoundError as fnf_error:
        print(fnf_error)


if __name__ == "__main__":
    ccwc()


'''
Step 2:
In this step, the goal is to support the command line option -l that outputs the number of lines in a file.

ccwc -l test.txt
'''

import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    

def main():
    if len(sys.argv) != 3:
        print("Usage: ccwc.py -l <file>")
        return
    
    option = sys.argv[1]
    if option != "-l":
        print(f"Unknown Option: {option}")
        return
    
    file_path = sys.argv[2]
    line_count = count_lines(file_path)

    if line_count is not None:
        print(f"{line_count} {file_path}")

if __name__ == "__main__":
    main()


'''
Step 3:
In this step, the goal is to support the command line option -w that outputs the number of words in a file.

ccwc -w test.txt
'''

import sys

def word_count(file_path):
    num_words = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                num_words += len(words)
        return num_words

    except FileNotFoundError:
        print(f"{file_path} not found! Please try again.")
        return None
    

def main():
    if len(sys.argv) != 3:
        print(f"Usage: ccwc.py -w <file path>")
    
    option = sys.argv[1]
    if option != "-w":
        print(f"Unknown Option: {option}")
    
    file_path = sys.argv[2]
    count_word = word_count(file_path)

    if count_word is not None:
        print(f"{count_word} {file_path}")

if __name__ == "__main__":
    main()


'''
Step 4:
In this step, the goal is to support the command line option -m that outputs the number of characters in a file.

ccwc -m test.txt
'''

import sys

def count_characters(file_path):
    char_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                char_count += len(line)
        return char_count
    
    except FileNotFoundError:
        print(f"{file_path} not found! Please try again!")
        return None
    

def main():
    if len(sys.argv) != 3:
        print(f"Usage: ccwc.py -m <file path>")

    option = sys.argv[1]
    if option != "-m":
        print(f"Unknown Option: {option}")

    file_path = sys.argv[2]
    count_char = count_characters(file_path)

    if count_char is not None:
        print(f"{count_char} {file_path}")

if __name__ == "__main__":
    main()


'''
Step 5:
In the step, the goal is to support the default option - i.e. no options are provided, which is equivalent 
to the -c, -l, and -w options. 

-c -> counts characters in the file.
-l -> counts number of lines in the file. 
-w -> count number of words in the file.

ccwc test.txt
'''


import sys

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line = file.readlines()
            return len(line)
    except FileNotFoundError:
        print(f"{file_path} not found! Please try again!")
        return None


def count_characters(file_path):
    char_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                char_count += len(line)
        return char_count
    except FileNotFoundError:
        print(f"{file_path} not found! Please try again!")
        return None


def count_words(file_path):
    word_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                word_count += len(words)
        return word_count
    except FileNotFoundError:
        print(f"{file_path} not found! Please try again!")
        return None



def main():
    if len(sys.argv) < 2:
        print("Usage ccwc.py [-c|-l|-m|-w] <file path>")
        return
    
    file_path = sys.argv[-1]

    if len(sys.argv) == 2:
        # no option provided, so calculate all
        line_count = count_lines(file_path)
        char_count = count_characters(file_path)
        word_count = count_words(file_path)

        if line_count is not None and char_count is not None and word_count is not None:
            print(f"Lines : {line_count}, Words: {word_count}, Characters: {char_count} {file_path}")
    else:
        option = sys.argv[1]
        if option == "-m":
            char_count = count_characters(file_path)
            if char_count is not None:
                print(f"{char_count} {file_path}")
        elif option == "-l":
            line_count = count_lines(file_path)
            if line_count is not None:
                print(f"{line_count} {file_path}")
        elif option == "-w":
            word_count = count_words(file_path)
            if word_count is not None:
                print(f"{word_count} {file_path}")
        else:
            print(f"Unknown Option: {option}")
            return

if __name__ == "__main__":
    main()


'''
Step 6:
The goal is to support being able to read from standard input if no filename is specified. 
'''

import sys

def count_lines(input_data):
    return len(input_data.splitlines())

def count_characters(input_data):
    return len(input_data)

def count_words(input_data):
    return len(input_data.split())

def read_input(file_path=None):
    if file_path:
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"{file_path} not found! Please try again!")
            return None
    else:
        # reading from std input
        print("Enter text (Press Ctrl + D to end input.)")
        return sys.stdin.read()
    
def main():
    if len(sys.argv) > 3:
        print("Usage: ccwc.py [-c|-l|-w] [<file_path>]")
        return
    
    if len(sys.argv) == 1:
        #no option or file path, read from stdin and do all counts
        input_data = read_input()
        if input_data is not None:
            print(f"Lines: {count_lines(input_data)}, Words: {count_words(input_data)}, Characters: {count_characters(input_data)}")
    else:
        option = sys.argv[1] if sys.argv[1].startswith("-") else None
        file_path = sys.argv[-1] if sys.argv[-1].startswith("-") else None

        input_data = read_input(file_path)
        if input_data is None:
            return
        if option is None:
            # no option is provided, calculate all counts
            print(f"Lines: {count_lines(input_data)}, Words: {count_words(input_data)}, Characters: {count_characters(input_data)} {file_path if file_path else ''}")
        elif option == "-m":
            print(f"{count_characters(input_data)}")


if __name__ == "__main__":
    main()
