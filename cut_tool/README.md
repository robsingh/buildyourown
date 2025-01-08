# Build Your Own - Cut Tool

## Description

Challenge is to build your own version of Cut tool.
Cut - cut out the selected portions of each line of a file.

## Step 1

In this step, the goal is to implement a simple version of cut that will open the provided tab separated file and print out the second field (-f1) from each line. 

**Output:**
```bash
cut -f1 sample.tsv
f1
1
6
11
16
21
```

## Step 2

In this step, the goal is to extend the functionality to support the -d option to allow user to specify what character to use as the delimiter between fields. If no delimiter is provided, then tab should still be used, we can test this first with a comma as the delimiter:

**Output:**
```bash
cut -f1 -d, fourchords.csv | head -n5
Song title
"10000 Reasons (Bless the Lord)"
"20 Good Reasons"
"Adore You"
"Africa"
```

Here we again seeing how the Unix command line tools can be chained (piped) together to create more powerful data processing pipelines. With the head command allowing us to limit the output to the first five lines.

Then check we still default to a tab:

```bash
cut -f1 sample.tsv
f0
0
5
10
15
20
```

## Step 3

In this step, the goal is to add support for the -f option. This option specifies a list of fields to be printed out. Output fields are separated by a single occurrence of the field delimiter character.

The field list is a comma or a whitespace separated list of fields, i.e. -f1,2 or -f "1 2". The first field is field number 1.

Here’s a couple of tests on this:

**Output:**
```bash
cut -f1,2 sample.tsv
f0      f1
0       1
5       6
10      11
15      16
20      21
```
and

```bash
cut -d, -f"1 2" fourchords.csv | head -n5
Song title,Artist
"10000 Reasons (Bless the Lord)",Matt Redman and Jonas Myrin
"20 Good Reasons",Thirsty Merc
"Adore You",Harry Styles
"Africa",Toto
```

## Step 4

In this step, the goal is to support reading from the standard input stream if no filename is provided or if the single dash is provided '-'.

**Output:**
```bash
tail -n5 fourchords.csv | cut -d, -f"1 2"
"Young Volcanoes",Fall Out Boy
"You Found Me",The Fray
"You'll Think Of Me",Keith Urban
"You're Not Sorry",Taylor Swift
"Zombie",The Cranberries
```

or

```bash
tail -n5 fourchords.csv | cut -d, -f"1 2" -
"Young Volcanoes",Fall Out Boy
"You Found Me",The Fray
"You'll Think Of Me",Keith Urban
"You're Not Sorry",Taylor Swift
"Zombie",The Cranberries
```