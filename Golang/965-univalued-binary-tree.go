/*
 * @lc app=leetcode.cn id=965 lang=golang
 *
 * [965] Univalued Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isUnivalTree(root *TreeNode) bool {
    return root == nil || (root.Left == nil || root.Val == root.Left.Val && isUnivalTree(root.Left)) && (root.Right == nil || root.Val == root.Right.Val && isUnivalTree(root.Right))
}
// @lc code=end

