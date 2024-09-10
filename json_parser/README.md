# Build your Own - JSON parser

## Description

Building a JSON parser is an easy way to learn about parsing techniques which are useful for everything from parsing simple data formats through to building a fully featured compiler for a programming language.

JSON - JavaScript Object Notation - a lightweight data-interchange format, which is widely used for transmitting data over the internet.

## Step 1
In this step your goal is to parse a valid simple JSON object, specifically: ‘{}’ and an invalid JSON file and correctly report which is which. So you should build a very simple lexer and parser for this step.

Your program should report to the standard output stream a suitable message and exit with the code 0 for valid and 1 for invalid.

You can test your code against the files in the folder tests/step1. Consider automating the tests so you can run them repeatedly as you progress through the challenge.

Solution Approach:
A lexer and a parser that can identify valid and invalid JSON objects.
Lexer : A function that reads a JSON string (in this challenge) and returns a list of tokens.
Parser : A function that takes these token and determines if they represent a valid JSON structure.

## Step 2