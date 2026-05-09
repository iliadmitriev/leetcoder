
type FindSumPairs struct {
	m1    map[int]int
	m2    map[int]int
	nums2 []int
}

func Constructor(nums1 []int, nums2 []int) FindSumPairs {
	m1 := make(map[int]int)
	m2 := make(map[int]int)
	for _, num := range nums1 {
		m1[num]++
	}

	for _, num := range nums2 {
		m2[num]++
	}

	return FindSumPairs{m1, m2, nums2}
}

func (this *FindSumPairs) Add(index int, val int) {
	this.m2[this.nums2[index]]--
	this.nums2[index] += val
	this.m2[this.nums2[index]]++
}

func (this *FindSumPairs) Count(tot int) int {
	total := 0

	for num, count := range this.m1 {
		if num >= tot {
			continue
		}

		if v, ok := this.m2[tot-num]; ok {
			total += count * v
		}
	}

	return total
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * obj := Constructor(nums1, nums2);
 * obj.Add(index,val);
 * param_2 := obj.Count(tot);
 */