#!/usr/bin/env python3

letter = 97

while letter < 123:
    if letter == 101:
        letter += 1
        continue
    if letter == 113:
        letter += 1
        continue
    print(chr(letter), end="")
    letter += 1
print("")
