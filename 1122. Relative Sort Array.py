# https://leetcode.com/problems/relative-sort-array/

'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        primary_order = {value: order for order, value in enumerate(arr2)}
        
        def decide_order(x):
            try:
                return(primary_order[x])
            except KeyError:
                primary_order[x] = 1001
                return 1001
            
        return sorted(sorted(arr1), key = lambda x: decide_order(x))
'''

from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        primary_sort = defaultdict(lambda : 1001)
        for value, order in enumerate(arr2):
            primary_sort[order] = value
        return sorted(sorted(arr1), key = lambda x: primary_sort[x])
        