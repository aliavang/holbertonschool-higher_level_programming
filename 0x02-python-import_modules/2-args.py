#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args > 0:
        if args == 2:
            print("{:d} argument:\n1: {:s}".format(args - 1, argv[1]))
        else:
            print("{:d} arguments:".format(args - 1))
            i = 1
            while i < args:
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1
    else:
        print("0 arguments.")
