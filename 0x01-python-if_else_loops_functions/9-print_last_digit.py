#!/usr/bin/python3
def print_last_digit(n):
    if n < 0:
        last_digit = -(n) % 10
    else:
        last_digit = n % 10

    print("{}".format(last_digit), end="")
    return (last_digit)
