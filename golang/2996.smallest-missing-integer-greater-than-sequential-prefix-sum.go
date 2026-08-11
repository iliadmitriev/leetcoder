func missingInteger(nums []int) int {
	n := len(nums)
	pre := nums[0]
    uniq := make(map[int]struct{})
    for _, v := range nums {
        uniq[v] = struct{}{}
    }

    for i := 1; i < n && nums[i -1] + 1 == nums[i]; i++ {
        pre += nums[i]
    }

    for {
        if _, ok := uniq[pre]; !ok {
            break;
        }

        pre++
    }
    return pre
}