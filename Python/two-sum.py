# -*- coding: utf-8 -*-


def two_sum(nums, target):
    """
    LeetCode problem 1: two sum
    :param nums: list[int]
    :param target: int
    :return:
    """
    for idx, num in enumerate(nums):
        another = target - num
        sub_nums = nums[idx + 1:]
        if another in sub_nums:
            another_idx = sub_nums.index(another)
            another_idx += idx + 1
            if another_idx > idx:
                return [idx, another_idx]
        else:
            continue
    return None


if __name__ == '__main__':
    nums = [3, 2, 4]
    result = two_sum(nums, 6)
    print(result)
