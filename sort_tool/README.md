# Build your Own - Sort Tool

## Description
The sort utility sorts text files by lines. A line is a record separated from the subsequent record by a newline.
For this challenge, we will ignore binary files. (We will implement it once the challenge is finished.)

Save the text as [test.txt](test.txt)

Use this expression
``` 
tr -s '[[:punct:][:space:]]' '\n' < test.txt |sed '/^[0-9]/d' > words.txt
```
to create a list of all the words in the file and save it as [words.txt](./words.txt)

## Step 1
In this step, the goal is to implement the essence of the sort program, we want to be able to run sort and have it open a file and output the lines in the
file sorted lexicographically.

```
sort words.txt | uniq | head -n5
A
ACTUAL
AGREE
AGREEMENT
AND
```
Here is my take on this challenge, a constructive feedback. You can see that the flag uniq is mentioned as a command line argument above, but
there is no mentioning of including unique functionality in Step 1. The unique functionality is mentioned to be included in Step 2. This is a great example of requirements
that could be clearer.

## Step 2


