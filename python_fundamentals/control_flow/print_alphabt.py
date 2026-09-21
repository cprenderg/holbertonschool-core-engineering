#!/usr/bin/env python3

letter = 97
output = ""

while letter < 123:
    if letter == 101:
        letter += 1
        continue
    if letter == 113:
        letter += 1
        continue
    output += chr(letter)
    letter += 1
print(output)
