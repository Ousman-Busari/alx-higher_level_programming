#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None:
        roman_int = {'M' : 100, 'D' : 500, 'C' : 100, 'L' : 50, \
                     'X' : 10, 'V' : 5, 'I' : 1}
        roman_digits = list(roman_string)
        integer = 0
        size = len(roman_digits)
        for i in range(size - 1):
            if roman_int[roman_digits[i]] < roman_int[roman_digits[i + 1]]:
                integer -= roman_int[roman_digits[i]]
            else:
                integer += roman_int[roman_digits[i]]

        integer += roman_int[roman_digits[size - 1]]
        return integer
    
