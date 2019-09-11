#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    number = number % 10
    print("{:d}".format(number), end="")
    return (number)
