import (
  "math"
)

type UF struct {
  cap int
  min []int
  par []int
}

func NewUF(cap int) *UF {
  par := make([]int, cap)
  minLen := make([]int, cap)

  for i := range cap {
    par[i] = i
    minLen[i] = math.MaxInt
  }

  return &UF{
    cap: cap,
    min: minLen,
    par: par,
  }
}

func (u *UF) find(x int) int {
  for x != u.par[x] {
    u.par[x] = u.par[u.par[x]]
    x = u.par[x]
  }

  return x
}

func (u *UF) join(x, y, w int) {
  parX, parY := u.find(x), u.find(y)

  minLen := min(u.min[parX], u.min[parY])
  u.par[parY] = parX
  u.min[parX] = min(w, minLen)
}

func (u *UF) getMinLen(x int) int {
  return u.min[u.find(x)]
}

func minScore(n int, roads [][]int) int {
    uf := NewUF(n)

    for _, v := range roads {
      uf.join(v[0] - 1, v[1] - 1, v[2])
    }

    return uf.getMinLen(n - 1)
}