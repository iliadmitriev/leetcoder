func maxSlidingWindow(nums []int, k int) []int {
    deque := make([]int, 0, len(nums)) // initial length 0, capacity n (all elements will be added and deleted once)
    result := make([]int, 0, len(nums) - k + 1)

    for i, num := range nums {

        for len(deque) > 0 && nums[deque[len(deque) - 1]] < num {
            deque = deque[:len(deque) - 1] // pop right
        }

        deque = append(deque, i) // append right

        if i + 1 < k {
            continue
        }

        result = append(result, nums[deque[0]])

        if deque[0] == i + 1 - k {
            deque = deque[1:] // pop left
        }
    }

    return result
}