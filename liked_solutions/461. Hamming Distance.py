#https://leetcode.com/problems/hamming-distance/
#https://leetcode.com/problems/hamming-distance/discuss/1042793/Python-one-liner


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')