# https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_num = {}
        # Created dict for for count of numbers: list of numbers
        for num in set(nums):
            count = nums.count(num)
            try:
                freq_num[count].append(num)
            except KeyError:
                freq_num[count] = [num]
        # Sort list based on the count of numbers
        freq_num = {k:v for k, v in sorted(freq_num.items(), key = lambda x: x[0])}
        
        # For numbers with the same frequency, sort the list in decreasing order
        for freq, num_list in freq_num.items():
            if len(num_list) >= 2:
                freq_num[freq] = sorted(num_list, reverse=True)
        
        # Convert the dict of freq: List[nums] to a list
        return [num for freq, num_list in freq_num.items()
                for num in num_list for _ in range(freq)]
