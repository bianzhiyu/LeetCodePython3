from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=len(matrix)
        for i in (k for k in range(l) if k<l-1-k):
            for j in (k for k in range(l) if i+k<l-1-i):
                matrix[i][i+j],matrix[i+j][l-1-i],matrix[l-1-i][l-1-i-j],matrix[l-1-i-j][i]=\
                    matrix[l-1-i-j][i],matrix[i][i+j],matrix[i+j][l-1-i],matrix[l-1-i][l-1-i-j]


