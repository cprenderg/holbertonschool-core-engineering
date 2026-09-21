#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

x = number
if number < 0:
    x = x * -1
while (x > 10):
    x = x % 10
if number < 0:
    x = x * -1
if x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")
elif x == 0:
    print(f"Last digit of {number} is {x} and is 0")
else:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")