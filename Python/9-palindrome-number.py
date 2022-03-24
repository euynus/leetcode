#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp, y = 0, x
        while y > 0:
            tmp = tmp * 10 + y % 10
            y //= 10
        return tmp == x
# @lc code=end

