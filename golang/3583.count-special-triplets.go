
import "slices"

type list []int

func (a list) searchLeft(x int) int {
	l, r := 0, len(a)
	var m int
	for l < r {
		m = (l + r) / 2

		if (a)[m] < x {
			l = m + 1
		} else {
			r = m
		}
	}

	return l
}

func (a list) searchRight(x int) int {
	l, r := 0, len(a)
	var m int

	for l < r {
		m = (l + r) / 2

		if a[m] > x {
			r = m
		} else {
			l = m + 1
		}
	}

	return l
}

func (a *list) append(x int) {
	*a = append(*a, x)
}

func (a *list) len() int {
	return len(*a)
}

func (a *list) iter() []int {
	return *a
}

func specialTriplets(nums []int) int {
	const MOD = int(1e9 + 7)
	cache := make(map[int][]int)
	total := 0

	for i, num := range nums {
		if _, ok := cache[num]; !ok {
			cache[num] = []int{}
		}

		cache[num] = append(cache[num], i)
	}

	if v, ok := cache[0]; ok {
		n := len(v)
		// C(n, 3) = n! / (3! * (n-3)!)
		// C(n, 3) = n * (n-1) * (n-2) / 6
		total += n * (n - 1) * (n - 2) / 6
		total %= MOD

		delete(cache, 0)
	}

	for num, v := range cache {
		x2 := num * 2
		nums, ok := cache[x2]
		if !ok {
			continue
		}

		for _, idx := range v {
			left, _ := slices.BinarySearch(nums, idx+1) // search right insert position
			right, _ := slices.BinarySearch(nums, idx)  // search left insert position

			right = len(nums) - right

			total += left * right
			total %= MOD
		}
	}

	return total
}
