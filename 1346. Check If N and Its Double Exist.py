#https://leetcode.com/problems/check-if-n-and-its-double-exist/
#https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/1123501/Python-Straight-Forward-Solution


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double_half_list = []
        for n in arr:
            if n in double_half_list:
                return True
            else:
                double_half_list.append(n*2)
                double_half_list.append(n/2)
        return False

                
