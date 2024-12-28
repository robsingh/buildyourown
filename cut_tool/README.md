# Build Your Own - Cut Tool

## Description

Challenge is to build your own version of Cut tool.
Cut - cut out the selected portions of each line of a file.

## Step 1

In this step, the goal is to implement a simple version of cut that will open the provided tab separated file and 
print out the second field (-f1) from each line. 

Output:
cut -f1 sample.tsv
f1
1
6
11
16
21

## Step 2

In this step, the goal is to extend the functionality to support the -d option to allow user to specify what character to use as the delimiter between fields. If no delimiter is provided, then tab should still be used, we can test this first with a comma as the delimiter:

cut -f1 -d, fourchords.csv | head -n5
Song title
"10000 Reasons (Bless the Lord)"
"20 Good Reasons"
"Adore You"
"Africa"

Here we again seeing how the Unix command line tools can be chained (piped) together to create more powerful data processing pipelines. With the head command allowing us to limit the output to the first five lines.

Then check we still default to a tab:

cut -f1 sample.tsv
f0
0
5
10
15
20

## Step 3

