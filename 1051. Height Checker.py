# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct_order = sorted(heights) 
        return len([1 for index, x in enumerate(heights) if x != correct_order[index]])
