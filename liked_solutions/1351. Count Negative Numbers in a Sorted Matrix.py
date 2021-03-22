#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/1110571/Python-one-liner


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([x for row in grid for x in row if x < 0])
