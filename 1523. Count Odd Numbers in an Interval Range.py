#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/discuss/1115248/Python-O(1)-and-O(n)Brute-Force-Solution

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low + 1) % 2 == 0:
            return int((high - low + 1) / 2)
        
        if low % 2 == 0 or low == 0:
            return int((high - low) / 2)
        
        return int((high - low) / 2) + 1
