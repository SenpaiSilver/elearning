#! /usr/bin/env python3

import sys

print("Hello World!"); # Print to STDOUT
print("Hello Error!", file=sys.stderr); # Print to STDERR
print("Hello", end="World!") # Print "Hello World!" with no newline
print() # Print just a newline
