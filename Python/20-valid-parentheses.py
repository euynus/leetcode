#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for c in s:
            if c in "([{":
                stack.append(c)
            if c == ")" and (not stack or stack.pop() != "("):
                return False
            if c == "]" and (not stack or stack.pop() != "["):
                return False
            if c == "}" and (not stack or stack.pop() != "{"):
                return False
        if stack:
            return False
        return True

# @lc code=end

