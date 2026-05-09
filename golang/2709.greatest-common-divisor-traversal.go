type UF struct {
    par []int
    rank []int
    size int
}

func NewUF(size int) *UF {
    par := make([]int, size)
    rank := make([]int , size)
    for i := range par { par[i] = i }
    for i := range rank { rank[i] = 1 }
    return &UF{par, rank, size}
}

func (f *UF) Len() int { return f.size }

func (f *UF) Find(x int) int {
    for x != f.par[x] {
        f.par[x] = f.par[f.par[x]]
        x = f.par[x]
    }
    return f.par[x]
}

func (f *UF) Join(x, y int) bool {
    px, py := f.Find(x), f.Find(y)
    if px == py {
        return false
    }

    if f.rank[py] > f.rank[px] {
        px, py = py, px
    }

    f.rank[px] += f.rank[py]
    f.rank[py] = 0
    f.par[py] = f.par[px]
    f.size--

    return true
}

func factors(num int, f func(int)) {
    lim := num
    for num % 2 == 0 {
        f(2)
        num /= 2
    }

    for i := 3; i * i <= lim; i += 2 {
        for num % i == 0 {
            f(i)
            num /= i
        }
    }

    if num > 2 {
        f(num)
    }
}

func canTraverseAllPairs(nums []int) bool {
    uf := NewUF(len(nums))

    factIdx := make(map[int]int)

    for i, num := range nums {
        factors(num, func(k int) {
            if idx, ok := factIdx[k]; ok {
                uf.Join(idx, i)
            } else {
                factIdx[k] = i
            }
        })
    }

    return uf.Len() == 1
}