import (
	"iter"
	"slices"
)

type maxFreqNums struct {
	freq []int
}

func NewMaxFreqNums(nums []int) *maxFreqNums {
	cnt := make([]int, len(nums))
	copy(cnt, nums)
	slices.Sort(cnt)

	return &maxFreqNums{
		freq: cnt,
	}
}

func (m *maxFreqNums) bisectLeft(target int) int {
	lo, hi := 0, len(m.freq)
	var mid int
	for lo < hi {
		mid = (lo + hi) / 2

		if m.freq[mid] < target {
			lo = mid + 1
		} else {
			hi = mid
		}

	}

	return lo
}

func (m *maxFreqNums) bisectRight(target int) int {
	lo, hi := 0, len(m.freq)

	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if m.freq[mid] > target {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}

func (m *maxFreqNums) All() iter.Seq2[int, int] {
	return func(yeild func(int, int) bool) {
		for i, num := range m.freq {
			yeild(i, num)
		}
	}
}

func maxFrequency(nums []int, k int, numOperations int) int {
	cnt := NewMaxFreqNums(nums)

	freq := make(map[int]int)
	for _, num := range nums {
		freq[num]++
	}

	maxFreq := 0

	for i, num := range cnt.All() {
		left := cnt.bisectLeft(num - k)
		right := cnt.bisectRight(num + k)

		window := right - left - freq[num]
		candidate1 := freq[num] + min(window, numOperations)
		maxFreq = max(maxFreq, candidate1)

		numNext := cnt.bisectRight(num + 2*k)
		candidate2 := min(numNext-i, numOperations)
		maxFreq = max(maxFreq, candidate2)
	}

	return maxFreq
}
