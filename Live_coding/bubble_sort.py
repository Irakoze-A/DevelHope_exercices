# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:50:45 2023

@author: OOK
"""

def bubble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

x = [3,5,6,4,2,7,56,7,54,2,3,5,6,7,6,4,4,6,7]


print(bubble_sort(x))