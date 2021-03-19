#https://leetcode.com/problems/find-lucky-integer-in-an-array/
#https://leetcode.com/problems/find-lucky-integer-in-an-array/discuss/1116844/Python-faster-than-90


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for num in sorted(set(arr), reverse=True):
            if num == arr.count(num):
                return num
        return -1
