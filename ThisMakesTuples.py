# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:48:02 2021

@author: DrVoidberg
"""

def my_enumerate(sequence, start=0):   # THIS MAKES TUPLES OUT OF STUFF 
     n = start
     for elem in sequence:
         yield n, elem
         n += 1
         
         
         