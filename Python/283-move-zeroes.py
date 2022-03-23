#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start1, start2 = 0, 1
        while start2 < len(nums):
            if nums[start1] != 0:
                start1 += 1
                start2 += 1
            else:
                if nums[start2] != 0:
                    nums[start2], nums[start1] = nums[start1], nums[start2]
                else:
                    start2 += 1
# @lc code=end

