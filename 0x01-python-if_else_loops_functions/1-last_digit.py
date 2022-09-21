#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    absolute_last_digit = -(number) % 10
else:
    absolute_last_digit = number % 10

if absolute_last_digit > 5:
    print(f"Last digit of {number} is {absolute_last_digit}",
          f"and is greater than 5")
elif absolute_last_digit == 0:
    print(f"Last digit of {number} is {absolute_last_digit} and is 0")
else:
    print(f"Last digit of {number} is {absolute_last_digit}",
          f"and is less than 6 and not 0")
