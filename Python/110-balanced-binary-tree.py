#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0

    def height(self, root: TreeNode):
        if root is None:
            return 0
        hl = self.height(root.left)
        hr = self.height(root.right)
        if hl == -1 or hr == -1 or abs(hl - hr) > 1:
            return -1
        return max(hl, hr) + 1
# @lc code=end

