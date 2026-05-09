func productExceptSelf(nums []int) []int {
  zeros := 0
  prod := 1
  j := 0
  res := make([]int, len(nums))

  for i, num := range nums {
    if num == 0 {
      zeros++
      j = i
    } else {
      prod *= num
    }
  }

  if zeros == 1 {
    res[j] = prod
    return res
  } else if zeros > 1 {
    return res
  }
    
  for i, num := range nums {
    res[i] = prod / num
  }

  return res
}