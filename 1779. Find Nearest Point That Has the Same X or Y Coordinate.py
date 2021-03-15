# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/discuss/1110608/Python-Solution-Using-defaultdict-Faster-Than-100

from collections import defaultdict
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distance_index = defaultdict(list)
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                distance_index[max(abs(x - point[0]), abs(y - point[1]))].append(index)
        
        if len(distance_index) == 0:
            return -1
        return min(distance_index[min(distance_index.keys())])
