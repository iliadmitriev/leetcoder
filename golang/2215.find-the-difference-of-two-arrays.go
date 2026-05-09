func findDifference(nums1 []int, nums2 []int) [][]int {
  m1 := make(map[int]bool)
  m2 := make(map[int]bool)

  for _, n := range nums1 {
    m1[n] = true
  }

  for _, n := range nums2 {
    m2[n] = true
  }

  res1 := make([]int, 0)
  for _, n := range nums1 {
    if _, ok := m2[n]; !ok {
      res1 = append(res1, n)
      m2[n] = true
    }
  }

  res2 := make([]int, 0)
  for _, n := range nums2 {
    if _, ok := m1[n]; !ok {
      res2 = append(res2, n)
      m1[n] = true
    }
  }

  return [][]int{res1, res2}  
}