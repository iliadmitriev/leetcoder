import (
  "slices"
)


func gcd1(a, b int) int {
  for b > 0 {
    a, b = b, a % b
  }

  return a
}

func gcd2(a, b int) int {
  for a != b {
    if a > b {
      a -= b
    } else {
      b -= a
    }
  }

  return a
}

func findGCD(nums []int) int {
  minVal := slices.Min(nums)
  maxVal := slices.Max(nums)    

  return gcd1(maxVal, minVal)
}