#!/usr/bin/python3

d = 122
for i in range(26):
    if (d > 90):
        print(chr(d), end="")
        d -= 33
    else:
        print(chr(d), end="")
        d += 31
