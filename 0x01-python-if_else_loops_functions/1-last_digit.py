#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0
    digit = (number * -1 % 10) * -1
else:
    digit = number % 10
varStr = "Last digit of"
if digit > 5:
    print(f"{varStr} {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"{varStr} {number:d} is {digit:d} and is 0")
elif digit < 6 and digit != 0:
    print(f"{varStr} {number:d} is {digit:d} and is less than 6 and not 0")
