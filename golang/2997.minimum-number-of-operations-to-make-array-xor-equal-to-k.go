package main

func minOperations(nums []int, k int) int {
	out := 0
	for _, num := range nums {
		out ^= num
	}

	if out == k {
		return 0
	}

	out = out ^ k
	n := 0
	for out > 0 {
		if out&1 == 1 {
			n++
		}
		out >>= 1
	}

	return n
}
