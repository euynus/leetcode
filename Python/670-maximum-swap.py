#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        i, length = 0, len(num_str) - 1
        while i < length:
            j = i + 1
            max_value = num_str[i]
            index = j
            while j <= length:
                if num_str[j] >= max_value:
                    max_value = num_str[j]
                    index = j
                j += 1
            if max_value > num_str[i]:
                num_str[i], num_str[index] = num_str[index], num_str[i]
                return int("".join(num_str))
            i += 1
        return num
# @lc code=end

