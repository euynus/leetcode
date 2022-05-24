/*
 * @lc app=leetcode.cn id=9 lang=golang
 *
 * [9] Palindrome Number
 */

// @lc code=start
func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    tmp, y := 0, x
    for ; y > 0; y /= 10 {
        tmp = tmp * 10 + y % 10
    }
    return tmp == x
}
// @lc code=end

