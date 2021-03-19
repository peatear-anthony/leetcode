#https://leetcode.com/problems/destination-city/
#https://leetcode.com/problems/destination-city/discuss/1116809/Python-Faster-than-90-or-Easy-to-Understand-Explanation


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = [path[0] for path in paths]
        for path in paths:
            if path[1] not in starting_cities:
                return path[1]
                
