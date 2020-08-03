# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:21:12 2020

@author: AE401
"""

E=input("enter your English score")
e=int(E)
M=input('enter your Math score')
m=int(M)
if e>=90 and m>=90:
    print('有獎品')
elif e<60 and m<60:
    print('有懲罰')
elif e<60 or m<60:
    print('再加油')