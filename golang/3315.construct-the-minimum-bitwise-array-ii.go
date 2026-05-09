/*

x:     10101110011
x+1:   10101110100
|:     10101110111 (num)


+1:    10101111000
~:     01010001000
&:     00000001000
>>:    00000000100
^:     10101110011


*/
func minBitwiseArray(nums []int) []int {
	ans := make([]int, 0, len(nums))

	for _, n := range nums {
		if n&1 == 1 {
			bit := (n + 1) & (^n)
			bit >>= 1

			x := n ^ bit
			ans = append(ans, x)

		} else {
			ans = append(ans, -1)
		}
	}

	return ans
}