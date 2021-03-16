# https://leetcode.com/problems/water-bottles/
# https://leetcode.com/problems/water-bottles/discuss/1112209/Python-Brute-Force-Solution


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = 0
        empty_bottles = 0
        while numBottles > 0:
            total_bottles += numBottles
            empty_bottles += numBottles
            numBottles = 0
            if empty_bottles >= numExchange:
                numBottles += int(empty_bottles / numExchange)
                empty_bottles = empty_bottles % numExchange
        return total_bottles
