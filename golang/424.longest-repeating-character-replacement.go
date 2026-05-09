const Base = byte('A')

type MinMap struct {
	cache [26]int
	total int
	max   int
}

func NewMinMap() *MinMap {
	return &MinMap{}
}

func (m *MinMap) Add(x byte) {
	m.total++
	m.cache[x - Base]++

	m.recalcMax()
}

func (m *MinMap) Discard(x byte) {
	m.total--
	m.cache[x - Base]--

	m.recalcMax()
}

func (m *MinMap) recalcMax() {
	m.max = -1
	for _, v := range m.cache {
		if m.max < v {
			m.max = v
		}
	}
}

// Get total count without max count
func (m *MinMap) GetCount() int {
	return m.total - m.max
}

func characterReplacement(s string, k int) int {
	win := NewMinMap()
	n := len(s)
	maxLen := 0

	for l, r := 0, 0; r < n; r++ {
		win.Add(s[r])

		for win.GetCount() > k {
			win.Discard(s[l])
			l++
		}

		maxLen = max(maxLen, r-l+1)
	}

	return maxLen
}