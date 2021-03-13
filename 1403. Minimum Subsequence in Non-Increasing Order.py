# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        nums.sort()
        total_sum = sum(nums)
        greater_sum = nums[-1]
        remaining_sum = total_sum - greater_sum
        index = len(nums) -2
        result = [greater_sum]
        
        while remaining_sum >= greater_sum:
            greater_sum += nums[index]
            remaining_sum = total_sum - greater_sum
            result.append(nums[index])
            index += -1
            
        return result
            
            
        