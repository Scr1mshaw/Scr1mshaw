# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:56:33 2021

@author: DrVoidberg
"""
import string
w = 0
attempts = 7 - int(w)
playing = True

theguessed = []
def hangmain():
    print("-------")  
    for row in range(5):
        if row == 0:
            print(" | ")      
        elif row == 1:
            if w == 7:
                print(" game over ")
            else:
                print(" 0 ")
        elif row == 2:
            if w == 4:
                print("/| ")
            elif w == 5:
                print(" | ")
            elif w >= 6:
                print("")
            else:
                print("/|\\")
        elif row == 3:
            if w >= 3:
                print("")
            else:
                print(" | ")
        elif row == 4:
            if w == 1:
                print("/ ")
            elif w >= 2:
                print("")
            else:
                print("/ \\")


def guessspace():
        newg1 = list("".join(map(str, guessword)))
        for idx,elem in enumerate(newg1):
            if elem not in theguessed:
                newg1[idx] = "_"
        finalgspace = ""
        for idf,y in enumerate(newg1):
                  finalgspace += y
        print(finalgspace)

            

        

        

guessword = str(input("Propose a word to guess: "))
wincount = int(len(guessword))

def guesscheck():
       global wincount
       if x in guessword:
           print("Correct!")
           theguessed.append(x)
           wincount = wincount - guessword.count(x)
       elif len(x) > 1:
            print("ONE letter")
       elif x not in list(string.ascii_lowercase) and x in list(string.ascii_uppercase):
            print("lowercase please")
       elif x not in list(string.ascii_lowercase) and x not in list(string.ascii_uppercase):
           print("one LETTER")
       else:
           global w
           w += 1
           print(w,"Incorrect, you have ",(7-w), "attempts left")

while playing is True:

        x = str(input("Guess one letter: "))
        guesscheck()
        hangmain()
        guessspace()
        if wincount == 0:
            print("That's the word, congratulations !")
            break

       

        
        