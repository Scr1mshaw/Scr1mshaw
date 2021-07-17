# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:09:50 2021

@author: DrVoidberg
"""
import string
import re




w = 0

player = 1

def guessspacer(word,x):
    global finalgspace
    for idx,elem in enumerate(word):
        if elem == " ":
            newg2[idx] = x
        else:
            newg2[idx] = "_"
    for y in newg2:
         finalgspace += y
    print(finalgspace)
# charstore = []

def lettercheck(n):
    newg = re.split(guessLetter,guessword)


    newg2 = list(" ".join(map(str, newg)))
    finalgspace = ""
       # if len(n) > 1:
       #     print("ONE letter")
       # elif n not in list(string.ascii_lowercase):
       #     print("one LETTER")
    if n in newg2:
        global finalgspace # maybe globalize in higher function scope
        global newg2
        for idx,elem in enumerate(newg2):
            if elem == " ":
                newg2[idx] = n
            else:
                newg2[idx] = "_"
        # for y in newg2:
        #     finalgspace += y
        print(newg2)
        print("correct")
    else:
        global w
        w += 1
        print(w,"Incorrect")



while player == 1:

    wordToGuess = str(input("Propose a word to guess: "))


    player += 1
    
    
# finalgspace = ""      if need global 

while player == 2:
    
    guessword = wordToGuess

    guessLetter = str(input("Guess a lowercase letter: "))
    

    # replace = "_"
    # newg = re.split(guessLetter,guessword)


    # newg2 = list(" ".join(map(str, newg)))
    # finalgspace = ""
    
    lettercheck(guessLetter)
    
    



