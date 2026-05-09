func divideArray(nums []int, k int) [][]int {
    sort.Ints(nums)
    n := len(nums)
    res := make([][]int, 0)

    for i := 0; i < n; i += 3 {
        if nums[i + 2] - nums[i] > k {
            return [][]int{}
        } 
        res = append(res, nums[i: i + 3])
    }

    return res
}