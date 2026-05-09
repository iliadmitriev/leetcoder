type topXsum struct {
	x   int
	cnt map[int]int
}

func NewTopXSum(x int) *topXsum {
	return &topXsum{
		x:   x,
		cnt: make(map[int]int),
	}
}

func (t *topXsum) add(num int) {
	t.cnt[num]++
}

func (t *topXsum) remove(num int) {
	t.cnt[num]--
}

func (t *topXsum) sum() int {
	res := 0

	tmp := make([][2]int, 0, len(t.cnt))

	for k, v := range t.cnt {
		tmp = append(tmp, [2]int{k, v})
	}

	slices.SortFunc(tmp, func(a, b [2]int) int {
		if a[1] == b[1] {
			return b[0] - a[0]
		}

		return b[1] - a[1]
	})

	x := min(t.x, len(tmp))

	for i := range x {
		res += tmp[i][0] * tmp[i][1]
	}

	return res
}

func findXSum(nums []int, k int, x int) []int {
	cnt := NewTopXSum(x)
	n := len(nums)
	res := make([]int, 0, n-k+1)

	for i := range k {
		cnt.add(nums[i])
	}

	res = append(res, cnt.sum())

	for i := k; i < n; i++ {
		cnt.remove(nums[i-k])
		cnt.add(nums[i])
		res = append(res, cnt.sum())
	}

	return res
}
