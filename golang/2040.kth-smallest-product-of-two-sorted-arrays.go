
// divIntFloor - divide two integers and round down towards left (minimum)
// and not to zero (fix intel compiler bug)
func divIntFloor(a, b int) int {
	c := a / b
	if a%b != 0 && ((a < 0) != (b < 0)) {
		c--
	}

	return c
}

// divIntCeil - divide two integers and round up towards right.
func divIntCeil(a, b int) int {
	c := a / b
	if a%b != 0 && ((a < 0) == (b < 0)) {
		c++
	}

	return c
}

// bisectLeftNeg - binary search left bound (support negative numbers)
func bisectLeftNeg(a []int, x int) int {
	l, r := 0, len(a)
	for l < r {
		m := l + (r-l)/2
		if a[m] < x {
			l = m + 1
		} else {
			r = m
		}
	}
	return l
}

// bisectRightNeg - binary search right bound (support negative numbers)
func bisectRightNeg(a []int, x int) int {
	l, r := 0, len(a)
	for l < r {
		m := l + (r-l)/2
		if x < a[m] {
			r = m
		} else {
			l = m + 1
		}
	}
	return l
}

func countProductsK(nums1 []int, nums2 []int, mid int) int {
	count := 0

	for _, num1 := range nums1 {
		if num1 > 0 {
			t := divIntFloor(mid, num1)
			count += bisectRightNeg(nums2, t)
		} else if num1 < 0 {
			t := divIntCeil(mid, num1)
			count += len(nums2) - bisectLeftNeg(nums2, t)
		} else {
			if mid >= 0 {
				count += len(nums2)
			}
		}
	}

	return count
}

func kthSmallestProduct(nums1 []int, nums2 []int, k int64) int64 {
	if len(nums1) > len(nums2) {
		return kthSmallestProduct(nums2, nums1, k)
	}
	limit := int(k)

	left, right := nums1[0]*nums2[0], nums1[0]*nums2[0]
	for _, v1 := range [2]int{0, len(nums1) - 1} {
		for _, v2 := range [2]int{0, len(nums2) - 1} {
			left = min(left, nums1[v1]*nums2[v2])
			right = max(right, nums1[v1]*nums2[v2])
		}
	}

	for left < right {
		mid := left + (right-left)/2
		cnt := countProductsK(nums1, nums2, mid)

		if cnt < limit {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return int64(left)
}
