#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    x = len(sys.argv) - 1
    n = len(sys.argv)

    if x == 0:
        print("{} arguments.".format(x))
    else:
        print("{} arguments:".format(x))
    
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
