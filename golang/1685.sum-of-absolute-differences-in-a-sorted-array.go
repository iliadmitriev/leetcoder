func getSumAbsoluteDifferences(nums []int) []int {
    n := len(nums)
    res := make([]int, n)

    if nums[0] == nums[n - 1] {
        return res
    }

    prefix := 0
    suffix := sum(nums)

    for i, num := range nums {
        res[i] = i * num - prefix + suffix - (n - i) * num
        prefix += num
        suffix -= num
    }
    return res
}

func sum(arr []int) int {
    res := 0
    for _, v := range arr {
        res += v
    }
    return res
}