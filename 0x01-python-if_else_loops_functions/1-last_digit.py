#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
varStr = "Last digit of"
if digit > 5:
    print(f"{varStr} {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"{varStr} {number:d} is {digit:d} and is 0")
elif digit < 0 and digit != 0:
    print(f"{varStr} {number:d} is {digit:d} and is less than 0")
