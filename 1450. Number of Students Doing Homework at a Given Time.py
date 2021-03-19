#https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
#https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/discuss/1116743/Python-faster-than-90


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        indexes = [index for index, start in enumerate(startTime)
                      if start <= queryTime]
        
        if len(indexes) == 0:
            return 0

        return len([1 for index in indexes
                   if endTime[index] >= queryTime])
        
