# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


for i in range(101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        continue
    elif (i % 5 == 0):
        print("Buzz")
        continue
    elif (i % 3 == 0):
        print("Fizz")
        continue
    print(i)