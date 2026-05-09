import (
    "sort"
)

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
    sort.Ints(arr)
    prev := 0
    for _, num := range arr {
        if (num > prev + 1) {
            num = prev + 1
        }
        prev = num
    }
    return prev
}