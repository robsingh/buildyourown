'''
we want to be able to run sort and have it open a file and output the lines in the file sorted lexicographically.

sort words.txt | uniq | head -n5
A
ACTUAL
AGREE
AGREEMENT
AND
'''

'''

notes:
1. let's begin with opening the file. - done
2. think how to sort the lines - thinking
'''

FILE_PATH = './test.txt'
def read_file():
    try:
        with open(FILE_PATH, 'r') as file:
            content = file.read().strip()
            if not content:
                print(f"The file is empty. Please verify the file before proceeding.")
                sys.exit(1)
            print(content)
    
    except FileNotFoundError:
        print(f"File not found.")




read_file()