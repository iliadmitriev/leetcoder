func findMaxConsecutiveOnes(nums []int) int {

  longest := 0
  cur := 0 // current number of ones

  for _, num := range nums {
    if num == 1 {
      cur++
    } else {
      cur = 0
    }
    longest = max(longest, cur)
  }
    
  return longest
}