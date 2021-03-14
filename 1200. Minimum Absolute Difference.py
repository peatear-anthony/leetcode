# https://leetcode.com/problems/minimum-absolute-difference/
# https://leetcode.com/problems/minimum-absolute-difference/discuss/1108716/Python-Solution-Easy-to-Understand


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dif_pair = {}
        arr.sort()

        for index, value in enumerate(arr[:-1], 1):
            pair = [value, arr[index]]
            dif = arr[index] - value
            try:
                dif_pair[dif].append(pair)
            except KeyError:
                dif_pair[dif] = [pair]

        return dif_pair[min(dif_pair.keys())]

