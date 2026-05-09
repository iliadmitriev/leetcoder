func largestPerimeter(nums []int) int64 {

    sort.Ints(nums)
    total := 0
    res := -1

    for _, num := range nums {

        if total > num {
            res = total + num
        }

        total += num
    }

    return int64(res)
}