/*
sorted:

a1 <= a2 ... b2 <= b1

a1 <= a2
b1 >= b2


a1 + b1 ? a2 + b

[2,2,2,5]
[2,4,4,5]

*/
func minPairSum(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    res := nums[0] + nums[n - 1]

    for i, j := 0, n - 1; i < j; i, j = i + 1, j - 1 {
        if res < nums[i] + nums[j] {
            res = nums[i] + nums[j]
        }
    }
    return res
}