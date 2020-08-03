# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:56:59 2020

@author: AE401
"""

h=input('enter your height')
w=input('enter your weight')
H=float(h)
W=float(w)
BMI=W//H**2
print(BMI)
float(BMI)
if BMI<18.5:
    print('體重不足')
elif BMI<24:
    print('正常')
elif BMI<27:
    print('體重')
elif BMI<30:
    print('輕度肥胖')
elif BMI<35:
    print('中度肥胖')
else:
    print('重度肥胖')