#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    nargs = len(argv)
    print("{:d} {:s}{:s}".format(nargs - 1, "argument" if nargs <= 2 else "arguments",
                                 "." if nargs == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
