#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    nargs = len(argv)
    if (nargs == 0):
        print("{:d} arguments.".format(nargs))
    elif (nargs == 1):
        print("{:d} argument:".format(nargs))
    else:
        print("{:d} arguments:".format(nargs))
        
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
