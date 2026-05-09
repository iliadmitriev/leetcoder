import (
    "sort"
)

func reductionOperations(nums []int) int {
    sort.Ints(nums)
    op := 0
    n := len(nums)

    for i := n - 1; i > 0; i-- {
        if nums[i] != nums[i - 1] {
            op += n - i;
        }
    }

    return op
}