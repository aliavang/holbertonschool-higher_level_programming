#!/usr/bin/python3
def safe_function(ftc, *args):
    import sys
    result = 0
    try:
        result = ftc(*args)
    except (ZeroDivisionError, IndexError) as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
    if result == 0:
        return None
    else:
        return result
