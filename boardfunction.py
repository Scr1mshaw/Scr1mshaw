# -*- coding: utf-8 -*-
"""
Created on Tue May 25 00:32:22 2021

@author: DrVoidberg
"""










def board(row,column):
    maxwidth = 40
    maxheight = 40 
    if row > maxheight or column > maxwidth:
        return False
    for r in range(row*2):
        if r % 2 == 0:
            for c in range(column*2):
                if c < ((column*2)-1):
                    if c % 2 == 0:
                        print("|",end="")
                    else:
                        print(" ",end="")
                else:
                    print("")
        else:
            print( ("-") * (column*2))

    return True




