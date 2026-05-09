func sumOfEncryptedInt(nums []int) int {
	res := 0

	for _, num := range nums {
		res += encryptMaxDigit(num)
	}

	return res
}

func encryptMaxDigit(num int) int {
	counter, maxDigit := 0, 0
	for num > 0 {
		maxDigit = max(maxDigit, num%10)
		num /= 10
		counter++
	}

	for counter > 0 {
		num = num*10 + maxDigit
		counter--
	}

	return num
}
