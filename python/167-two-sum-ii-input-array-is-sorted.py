#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 1, len(numbers)
        while start < end:
            tmp = target - numbers[start - 1]
            if tmp == numbers[end - 1]:
                return start, end
            elif tmp > numbers[end - 1]:
                start += 1
            else:
                end -= 1
# @lc code=end

