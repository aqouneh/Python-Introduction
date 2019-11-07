# computes and records final grades

# input line format:

# name and misc. info, e.g. class level
# Final Report grade
# Midterm grade
# Quiz grades
# Homework grades

# e.g.
#
# John Paul Jones SR LCSI 70 A 50 B 69 B+ B+ A 3.52 B+

# comment lines, beginning with #, are ignored for computation but are
# printed out; thus various notes can be put in comment lines; e.g.
# notes on missed or makeup exams

# usage:

# python FinalGrades.py input_file nq nqd nh wts

# where there are nq Quizzes, the lowest nqd of which will be
# deleted; nh Homework assignments; and wts is the set of weights
# for Final Report, Midterm, Quizzes and Homework

# outputs to stdout the input file with final course grades appended;
# the latter are numerical only, allowing for personal inspection of
# "close" cases, etc.

import sys

def convertltr(lg): # converts letter grade lg to 4-point-scale
    if lg == ’F’: return 0
    base = lg[0]
    olg = ord(base)
    if len(lg) > 2 or olg < ord(’A’) or olg > ord(’D’):
    print lg, ’is not a letter grade’
    sys.exit(1)
    grade = 4 - (olg-ord(’A’))
    if len(lg) == 2:
        if lg[1] == ’+’: grade += 0.3
        elif lg[1] == ’-’: grade -= 0.3
        else:
            print lg, ’is not a letter grade’
            sys.exit(1)
    return grade

def avg(x,ndrop):
    tmp = []
    for xi in x: tmp.append(convertltr(xi))
    tmp.sort()
    tmp = tmp[ndrop:]
    return float(sum(tmp))/len(tmp)

def main():
    infile = open(sys.argv[1])
    nq = int(sys.argv[2])
    nqd = int(sys.argv[3])
    nh = int(sys.argv[4])
    wts = []
    for i in range(4): wts.append(float(sys.argv[5+i]))
    for line in infile.readlines():
        toks = line.split()
        if toks[0] != ’#’:
            lw = len(toks)
            startpos = lw - nq - nh - 3
    # Final Report
    frgrade = convertltr(toks[startpos])
    # Midterm letter grade (skip over numerical grade)
    mtgrade = convertltr(toks[startpos+2])
    startquizzes = startpos + 3
    qgrade = avg(toks[startquizzes:startquizzes+nq],nqd)
    starthomework = startquizzes + nq
    hgrade = avg(toks[starthomework:starthomework+nh],0)
    coursegrade = 0.0
    coursegrade += wts[0] * frgrade
    coursegrade += wts[1] * mtgrade
    coursegrade += wts[2] * qgrade
    coursegrade += wts[3] * hgrade
    print line[:len(line)-1], coursegrade
    else:
    print line[:len(line)-1]

    if __name__ == ’__main__’:
main()
