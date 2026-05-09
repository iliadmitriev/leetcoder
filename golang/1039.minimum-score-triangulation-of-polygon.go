
const (
	INF   = int(0x7FFFFFFFFFFFFFFF)
	EMPTY = -1
)

type TriangleDP struct {
	cache  [][]int
	values []int
}

func NewTriangleDP(n int, values []int) *TriangleDP {
	cache := make([][]int, n)

	for i := range n {
		cache[i] = make([]int, n)
		for j := range n {
			cache[i][j] = EMPTY
		}
	}

	return &TriangleDP{
		cache:  cache,
		values: values,
	}
}

func (t *TriangleDP) dfs(i, j int) int {
	if j-i < 2 {
		return 0
	}

	if j-i == 2 {
		return t.values[i] * t.values[i+1] * t.values[j]
	}

	if t.cache[i][j] != EMPTY {
		return t.cache[i][j]
	}

	res := INF

	for k := i + 1; k < j; k++ {
		res = min(res, t.dfs(i, k)+t.dfs(k, j)+t.values[i]*t.values[k]*t.values[j])
	}

	t.cache[i][j] = res
	return res
}

func minScoreTriangulation(values []int) int {
	return NewTriangleDP(len(values), values).dfs(0, len(values)-1)
}
