
// Count number of occurences in contiguous subarrays
// https://math.stackexchange.com/questions/1941224/number-of-occurrences-in-contiguous-subarrays
// convolution k * (n - k - 1)
// shift left (+1) -> (k + 1) * (n- k) + 1
// divide by 2 (odd) -> ((k + 1) * (n - k) + 1) / 2

func sumOddLengthSubarrays(arr []int) int {
	res := 0
	n := len(arr)

	for i, num := range arr {
		cnt := ((i+1)*(n-i) + 1) / 2
		res += cnt * num
	}
	return res
}
