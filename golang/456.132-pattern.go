import (
    "math"
)

func find132pattern(nums []int) bool {
    lastMin := math.MaxInt
    stack := make([][2]int, 0, len(nums))

    for _, num := range nums {

        for len(stack) > 0 && stack[len(stack) - 1][0] <= num {
            stack = stack[:len(stack) - 1]
        }

        if len(stack) > 0 && stack[len(stack) - 1][0] > num && stack[len(stack) - 1][1] < num {
            return true
        }

        stack = append(stack, [2]int{num, lastMin})
        lastMin = min(lastMin, num)
    }

    return false
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}