func subarraySum(nums []int, k int) int {
    prefix := map[int]int{0: 1}
    acc := 0
    count := 0

    for _, num := range nums {
        acc += num
        diff := acc - k
        count += prefix[diff]

        prefix[acc]++
    }


    return count
}