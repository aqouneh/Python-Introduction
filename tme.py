# reads in the text file whose name is specified on the command line,
# and reports the number of lines and words

import sys

def checkline():
    global l            # global variables
    global wordcount
    w = l.split()
    wordcount += len(w)

wordcount = 0           # Variables are not declared in Python
f = open(sys.argv[1])
flines = f.readlines()
linecount = len(flines) # len() returns number of elements in a list
for l in flines:
    checkline()
print linecount, wordcount
