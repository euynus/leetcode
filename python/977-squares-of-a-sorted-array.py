#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        result = []
        while start <= end:
            sq_start = nums[start] ** 2
            sq_end = nums[end] ** 2
            if sq_start > sq_end:
                result.append(sq_start)
                start += 1
            else:
                result.append(sq_end)
                end -= 1

        return reversed(result)
# @lc code=end

