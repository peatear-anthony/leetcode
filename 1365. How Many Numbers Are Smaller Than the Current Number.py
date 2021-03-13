# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        encounter = {}
        result = []
        for num in nums:
            if(num in encounter):
                result.append(encounter[num])
            else:
                num_smaller_than = len([1 for x in nums if num > x])
                result.append(num_smaller_than)
                encounter[num] = num_smaller_than
                
        return(result)
        '''
        dic1 = {}
        nums1 = sorted(nums, reverse=True)
        for index in range(0, len(nums1) - 1):
            if nums1[index] == nums1[index + 1]:
                continue
            dic1[nums1[index]] = len(nums1) - index -1    
        dic1[nums1[-1]] = 0
        return([dic1[x] for x in nums])
            