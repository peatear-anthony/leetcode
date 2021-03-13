# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dim = len(mat)
        diagonal = sum(mat[i][i] + mat[i][dim - 1 - i]  for i in range(dim))
        if dim % 2 != 0:
            return diagonal - mat[int((dim-1)/2)][int((dim-1)/2)] 
        return diagonal 