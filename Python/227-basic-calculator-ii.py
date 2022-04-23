#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] Basic Calculator II
#
# @lc code=start

class Solution:
    def calculate(self, s: str) -> int:
        tmp = 0
        pre_sign = "+"
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] != " " and s[i].isdigit():
                tmp = tmp * 10 + ord(s[i]) - ord("0")
            if s[i] in '+-*/' or i == n - 1:
                if pre_sign == "+":
                    stack.append(tmp)
                elif pre_sign == "-":
                    stack.append(-tmp)
                elif pre_sign == "*":
                    stack.append(stack.pop() * tmp)
                else:
                    stack.append(int(stack.pop() / tmp))
                pre_sign = s[i]
                tmp = 0
        return sum(stack)

# @lc code=end

