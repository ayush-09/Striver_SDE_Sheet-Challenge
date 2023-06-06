# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:52:13 2023

@author: ayush
"""

def generate(numRows):
    res=[[1]]
    for i in range(numRows-1):
        te=[0]+res[-1]+[0]
        row=[]
        for j in range(len(res[-1])+1):
            row.append(te[j]+te[j+1])
        res.append(row)
    return res

print(generate(5))                

