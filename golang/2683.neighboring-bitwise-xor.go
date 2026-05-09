func doesValidArrayExist(derived []int) bool {
	cur := 0
	for _, v := range derived {
		cur ^= v
	}
	return cur == 0
}
