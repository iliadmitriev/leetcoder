import (
    "slices"
)

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
    slices.Sort(arr)
    prev := 0

    for _, num := range arr {
      prev = min(prev + 1, num)
    }
    
    return prev
}