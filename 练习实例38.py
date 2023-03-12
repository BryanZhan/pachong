"""
题目：求一个3*3矩阵主对角线元素之和。
求一个3*3矩阵主对角线元素之和。#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print (sum)

"""