func majorityElement(nums []int) []int {
    freq := make(map[int]int)
    thr := len(nums) / 3
    res := make([]int, 0, 2)

    for _, num := range nums {
        freq[num]++
    }

    for num, count := range freq {
        if count > thr {
            res = append(res, num)
        }
    }
    return res
}