func containsNearbyDuplicate(nums []int, k int) bool {
  n := len(nums)
  cache := make(map[int]struct{})

  for i := 0; i < n; i++ {
    if _, ok := cache[nums[i]]; ok {
      return true
    }
    
    cache[nums[i]] = struct{}{}

    if i - k >= 0 {
      delete(cache, nums[i - k])
    }
  }

  return false
}