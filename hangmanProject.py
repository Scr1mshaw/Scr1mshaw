# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:33:49 2021

@author: DrVoidberg
"""

#melting the hangman from input

#  |    
#  0
# /|\
#  |
# / \


w = 0 # if wrong increment, every increment removes a bodypart 



    # also GAME OVER goes here 

def hangmain():
    print("-------")  
    for row in range(5):
        if row == 0:
            print(" | ")      
        elif row == 1:
            if w == 7:   # ALSO GAME OVER
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

hangmain()
