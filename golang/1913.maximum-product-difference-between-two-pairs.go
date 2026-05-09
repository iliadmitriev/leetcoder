import (
    "math"
)

func maxProductDifference(nums []int) int {
    max1, max2 := math.MinInt, math.MinInt
    min1, min2 := math.MaxInt, math.MaxInt

    for _, n := range nums {
        if max1 < n {
            max1, max2 = n, max1
        } else if max2 < n {
            max2 = n
        }

        if min1 > n {
            min1, min2 = n, min1
        } else if min2 > n {
            min2 = n
        }
    }

    return (max1 * max2) - (min1 * min2)
}