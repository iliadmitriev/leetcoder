/*
prefix
======

[2,3,1,2,4,3] t=7
[2,5,6,8,12,15]

[1,4,4] t=4
[1,5,9]
[0:-1, 1:0, 5:1, 9:2]

[12] t=12
[0:-1]
*/
func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	minSub := n + 1
  cur := 0

  for i, j := 0, 0; i < n; i++ {
    cur += nums[i]

    for j <= i && cur >= target {
      minSub = min(minSub, i - j + 1)
      cur -= nums[j]
      j++
    }
  }

  if minSub > n {
    return 0
  }

	return minSub
}