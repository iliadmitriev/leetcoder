type DSU struct {
    size int
    parent []int
    rank []int
}

func NewDSU(size int) *DSU {
    parent := make([]int, size)
    rank := make([]int, size)

    for i := 0; i < size; i++ {
        parent[i] = i
        rank[i] = 1
    }

    return &DSU{ size, parent, rank }
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

    if d.rank[par_y] > d.rank[par_x] {
        par_x, par_y = par_y, par_x
    }
    d.parent[par_y] = par_x
    d.rank[par_x] += d.rank[par_y]
    d.rank[par_y] = 0
    return true
}

func (d *DSU) components() []int {
    count := 0
    maxSize := 0
    sizes := make(map[int]int)

    for i := range d.parent {
        key := d.find(i)
        if i == key {
            count++
        }
        sizes[key]++
    }

    for _, v := range sizes {
        if v > maxSize {
            maxSize = v
        }
    }

    return []int{count, maxSize}
}

func getMask(s string) int {
    res := 0
    for _, r := range s {
        res |= 1 << (r - 'a')
    }
    return res
}

func groupStrings(words []string) []int {
    n := len(words)
    dsu := NewDSU(n)
    cache := make(map[int]int)

    for i, word := range words {
        mask := getMask(word)

        if j, ok := cache[mask]; ok {
            dsu.join(i, j)
        } else {
            cache[mask] = i
        }

        for j := 0; j < 26; j++ {
            if mask & (1 << j) == 0 {
                continue
            }

            key := mask ^ (1 << j)
            if j, ok := cache[key]; ok {
                dsu.join(i, j)
            } else {
                cache[key] = i
            }

        }
    }

    return dsu.components()
}