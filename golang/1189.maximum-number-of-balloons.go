func maxNumberOfBalloons(text string) int {
	res := len(text)
	count := make([]int, 26)

	for _, c := range text {
		count[c-'a']++
	}

	res = min(res, count[1])
	res = min(res, count[0])
	res = min(res, count[11]/2)
	res = min(res, count[14]/2)
	res = min(res, count[13])

	return res
}
