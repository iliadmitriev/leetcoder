func getDominantElement(arr []int) int {
	cnt, res := 0, -1
	for _, v := range arr {
		if cnt == 0 {
			res = v
		}
		if v == res {
			cnt++
		} else {
			cnt--
		}
	}

	return res
}

func getCountOf(arr []int, v int) int {
	cnt := 0
	for _, num := range arr {
		if num == v {
			cnt++
		}
	}
	return cnt
}

func minimumIndex(nums []int) int {
	dom := getDominantElement(nums)
	left, right := 0, getCountOf(nums, dom)
	n := len(nums)

	if 2*right <= n {
		return -1
	}

	for i, v := range nums {
		if v == dom {
			left++
			right--
		}

		if 2*left > i+1 && 2*right > n-i-1 {
			return i
		}
	}

	return -1
}
