"""
题目：利用递归方法求5!。
利用递归方法求5!。#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum
 
print (fact(5))

"""