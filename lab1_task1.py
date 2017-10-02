#!/usr/bin/env python

def f_to_c(F):
    return 5 * (int(F)-32) / 9

def c_to_f(C):
    return ((9 * int(C)) + 160) / 5

while True:
    try:
        inputtype = raw_input("Input type: ").upper().strip()
        if not inputtype in "CF":
            print "Invalid type"
            raise ValueError("Invalid type")
 
        degree = raw_input("Degree: ").strip()
        res = 0
        if inputtype == "C":
            res = c_to_f(degree)
        else:
            res = f_to_c(degree)
        print "Result: %d" % res
    except ValueError:
        print "Invalid type: "
        continue
    except (EOFError, KeyboardInterrupt):
        break 

