func numSimilarGroups(strs []string) int {
    n := len(strs)
    dsu := NewDSU(n)

    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if similar(strs[i], strs[j]) {
                _ = dsu.join(i, j)
            }
        }
    }

    return dsu.count()
}

func similar(s1, s2 string) bool {
    if s1 == s2 {
        return true
    }
    replacements := 0
    n := min(len(s1), len(s2))
    for i := 0; i < n; i++ {
        if s1[i] != s2[i] {
            replacements++
        }

        if replacements >= 3 {
            return false
        }
    }
    return true
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

type DSU struct {
    parent []int
    rank []int
}

func NewDSU(size int) *DSU {
    rank := make([]int, size)
    parent := make([]int, size)
    for i := range rank {
        parent[i] = i
        rank[i] = 1
    }

    return &DSU{ parent, rank }
}

func (d *DSU) find(x int) int {
    for x != d.parent[x] {
        d.parent[x] = d.parent[d.parent[x]]
        x = d.parent[x]
    }
    return x
}

func (d *DSU) join(x, y int) bool {
    par_x, par_y := d.find(x), d.find(y)

    if par_x == par_y {
        return false
    }

    if d.rank[par_x] < d.rank[par_y] {
        par_x, par_y = par_y, par_x
    }

    d.parent[par_y] = d.parent[par_x]
    d.rank[par_x] += d.parent[par_y]
    d.rank[par_y] = 0
    return true
}

func (d *DSU) count() int {
    count := 0
    for i := range d.parent {
        if d.find(i) == i {
            count++
        }
    }
    return count
}