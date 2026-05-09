// [*,0,*]
// [1,0,*,0,*,0,1]
// [1,0,*,0,*]
func canPlaceFlowers(flowerbed []int, n int) bool {
	k := len(flowerbed)
	i := 0

	for i < k && n > 0 {
		if (i-1 < 0 || flowerbed[i-1] == 0) && flowerbed[i] == 0 && (i+1 >= k || flowerbed[i+1] == 0) {
			n--
			i += 2
		} else {
			i += 1
		}
	}

	return n == 0
}