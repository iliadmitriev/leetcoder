import (
    "math"
)

func maxProduct(nums []int) int {
    max1, max2 := math.MinInt, math.MinInt

    for _, num := range nums {
        if num > max1 {
            max2 = max1
            max1 = num
        } else if num > max2 {
            max2 = num
        }
    }

    return (max1 - 1) * (max2 - 1)
}