#https://leetcode.com/problems/remove-outermost-parentheses/
#https://leetcode.com/problems/remove-outermost-parentheses/discuss/1020703/Python-simple-solution-with-explanation


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result =  ''
        depth = 0
        for index in range(0, len(S) - 1):
            char = S[index]
            if depth != 0:
                result += char
            if char == "(" and S[index + 1] == "(":
                depth += 1
            elif char == ")" and S[index + 1] == ")":
                depth -= 1
        return result