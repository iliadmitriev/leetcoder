func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {
    ops := k1 + k2
    n := len(nums1)
    mx := 0

    abs := func(x int) int {
      if x < 0 {
        return -x
      }
      return x
    }

    for i := range n {
      v := abs(nums1[i] - nums2[i])
      mx = max(mx, v)
      nums1[i] = v
    }

    diffCount := make([]int, mx + 1)
    for _, diff := range nums1 {
      diffCount[diff]++
    }

    var op int
    for diff := mx; diff > 0 && ops > 0; diff-- {
        op = min(ops, diffCount[diff])

        ops -= op
        diffCount[diff] -= op
        diffCount[diff - 1] += op
    }

    res := 0

    for diff := mx; diff > 0; diff-- {
      res += diff * diff * diffCount[diff]
    }

    return int64(res)
}