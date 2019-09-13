#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args > 0:
        if args == 2:
            print("{:d} argument:\n1: {:s}".format(args, argv[1]))
        else:
            print("{:d} arguments:".format(args))
            i = 1
            while i < args:
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1
    else:
        print("{:d} arguments.".format(args))
