# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:52:13 2023

@author: ayush
"""

def setZeros(matrix):
	# Write your code here.
    #forward traversal
    col=1
    row=len(matrix)
    cols=len(matrix[0])
    for i in range(row):
        if matrix[i][0]==0:
            col=0
        for j in range(1,cols):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0 #leftmost and topmost
    
    #backward traversal
    for i in range(row-1,-1,-1):
        for j in range(cols-1,0,-1):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
        if col==0:
            matrix[i][0]=0
    return matrix
    
print(setZeros([[1,1,1],[1,0,1],[1,1,1]]))