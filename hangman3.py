# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 00:58:07 2021

@author: DrVoidberg
"""

import re
guessword = "aaabbbabc"
theguessed = []
while True:

    
    x = str(input("guess "))
    theguessed.append(x)
    xcounter = re.compile('|'.join(theguessed))

 
    
    newg = re.split(xcounter,guessword)
    
    
    newg2 = list(" ".join(map(str, newg)))
    print(newg2)
    finalgspace = ""
    
    def guessspacer(word):
        global finalgspace
        global newg
        global theguessed
        for idx,elem in enumerate(newg2):
            if elem == " ":
                newg2[idx] = x
            else:
                newg2[idx] = "_"
        for idf,y in enumerate(newg2):
              finalgspace += y
        print(finalgspace)
        
    
    guessspacer(guessword)
    


# guess a
# [' ', 'b', 'c', 'c', 'c', ' ', ' ', 'b', ' ']
# a____aa_a

 # - > replace whitespaces with a filler in newg2

# guess b
 # - > ignore filler, replace in finalspace 
# ['a', ' ', 'c', 'c', 'c', 'a', 'a', ' ', 'a']
# _b_____b_
# 




