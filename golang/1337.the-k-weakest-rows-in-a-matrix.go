import (
    "container/heap"
)


type Row struct {
    countOnes int
    index int
}

type Rows []Row

// len, swap, less callbacks
func (r Rows) Len() int { return len(r) }
func (r Rows) Swap(i, j int) { r[i], r[j] = r[j], r[i] }
func (r Rows) Less(i, j int) bool {
    return r[i].countOnes < r[j].countOnes ||
        (r[i].countOnes == r[j].countOnes &&
            r[i].index < r[j].index)
}

// push, pop contaner methods
func (r *Rows) Push(x interface{}) {
    *r = append(*r, x.(Row))
}

func (r *Rows) Pop() interface{} {
    old := *r
    n := len(old)
    x := old[n - 1]
    *r = old[0: n - 1]
    return x
}

func getZero(row []int) int {
    lo, mid, hi := 0, 0, len(row)

    for lo < hi {
        mid = (lo + hi) / 2
        if row[mid] == 0 {
            hi = mid
        } else {
            lo = mid + 1
        }
    }

    return lo
}

func kWeakestRows(mat [][]int, k int) []int {
    hq := &Rows{}

    for i, row := range mat {
        heap.Push(hq, Row{getZero(row), i})
    }

    fmt.Println(hq)

    res := make([]int, 0, k)

    for ; k > 0; k-- {
        res = append(res, heap.Pop(hq).(Row).index)
    }

    return res;
}