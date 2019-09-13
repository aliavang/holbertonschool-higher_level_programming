#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args > 0:
        if args == 1:
            print("{:d} argument:\n1: {:s}".format(args, argv[1]))
        else:
            print("{:d} arguments:".format(args))
            for i in range(args):
                print("{:d}: {:s}".format(i + 1, argv[i + 1]))
    else:
        print("{:d} arguments.".format(args))
