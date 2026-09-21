#!/usr/bin/env python3

letter = 97

while letter:
    if letter == 101:
        letter += 1
        continue
    if letter == 113:
        letter += 1
        continue
    if letter == 123:
        letter = 10
    print("{:c}".format(letter), end="")
    if letter == 10:
        break
    letter += 1
