func firstStableIndex(nums []int, k int) int {
    n := len(nums)

    vmax := nums[0]
    
    vmin := make([]int, n)
    vmin[n - 1] = nums[n - 1]
    for i := n - 2; i >= 0; i-- {
      vmin[i] = min(vmin[i + 1], nums[i])
    }

    for i := 0; i < n; i++ {
      vmax = max(vmax, nums[i])

      if vmax - vmin[i] <= k {
        return i
      }
    }

    return -1
}