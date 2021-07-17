# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:07:15 2021

@author: DrVoidberg
"""


import re  # used this to check win patterns 


currentfield = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

player = 1

def gg(): # stops the game when win condition is met
    if boardstringP1(currentfield) is True or boardstringP2(currentfield) is True:
        return True
    return False



#checks if a move is legal (column not full)


def colAvail(column):
    if all(x != " " for x in currentfield[column]):
        return False
    else:
        return True


# makes displayable board out of currentfield list


def colmaker(field):
    for num in range(6):
        for col in field:
           print(col[num],end=" | ")
        print('')


# WINCHECK player 1  -  only coin characters differ 


def boardstringP1(board):
    bstring = []
    for f in board:
        for g in f:
            bstring.append(g)
    astring = "".join([str(item) for item in bstring])
    wstring = astring.replace(" ",".")
    winside = re.search("xxxx",wstring)
    wintop = re.search("x......x......x......x",wstring)
    winlr = re.search("x.......x.......x........x",wstring)
    winrl = re.search("...x.....x.....x.....x",wstring)
    if winside or wintop or winlr or winrl:
        print("GG, you won")
        return True
    return False


# WINCHECK player 2  -  only coin characters differ 


def boardstringP2(board):
    bstring = []
    for f in board:
        for g in f:
            bstring.append(g)
    astring = "".join([str(item) for item in bstring])
    wstring = astring.replace(" ",".")
    winside = re.search("oooo",wstring)
    wintop = re.search("o......o......o......o",wstring)
    winlr = re.search("o.......o.......o........o",wstring)
    winrl = re.search("...o.....o.....o.....o",wstring)
    if winside or wintop or winlr or winrl:
        print("GG, you won")
        return True
    return False
   
   
# MAIN of GAME, field converter to something displayable, player input alternator, win check implement 

while gg() is False:
    if player == 1:
        column = int(input("Col number, player 1: "))
        if colAvail(column) is True:
            emptyIndices = []
            maxEmpty = 0
            for idx,c in enumerate(currentfield[column]):
                if c == " ":
                    emptyIndices.append(idx)
            for e in emptyIndices:
                if e is max(emptyIndices):
                    maxEmpty = e
            currentfield[column][maxEmpty] = "x"
            boardstringP1(currentfield)
            gg()
            colmaker(currentfield)    #   PRINT BOARD HERE 
            player += 1
        else:
            print("it's full, pick another")
    elif player == 2:
        column = int(input("Col number?, player 2: "))
        if colAvail(column) is True:
            emptyIndices = []
            maxEmpty = 0
            for idx,c in enumerate(currentfield[column]):
                if c == " ":
                    emptyIndices.append(idx)
            for e in emptyIndices:
                if e is max(emptyIndices):
                    maxEmpty = e
            currentfield[column][maxEmpty] = "o"
            boardstringP2(currentfield)
            gg()
            colmaker(currentfield)    # PRINT BOARD HERE
            player -= 1
        else:
            print("it's full, pick another")
    else:
        break





