# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:36:22 2021

@author: DrVoidberg
"""

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# maximum length 16 characters.

#string.ascii_uppercase
#string.ascii_lowercase
#string.punctuation
#string.digits



def passcheck(a):
    if len(a) < 6:
        print("too short")
    elif len(a) > 16:
        print("too long")
    else:
        if not any(char.isdigit() for char in a):
            print('Password should have at least one numeral')
        elif not any(char.isnumeric() for char in a):
            print('needsnums')
        elif not any(char.isupper() for char in a):
            print('needs upper')
        elif not any(char.islower() for char in a):
            print('need lower')
        else:
            print("good to go")

passcheck("ffTffffff")