// Top 3 unique positive integers accumulator
type TopThree struct {
  a, b, c int // a > b > c
}

func (t *TopThree) Put(x int) {
  switch {
    case x > t.a:
      t.a, t.b, t.c = x, t.a, t.b
    case x != t.a && x > t.b:
      t.b, t.c = x, t.b
    case x != t.a && x != t.b && x > t.c:
      t.c = x
  }
}

func (t *TopThree) Get() []int {
  res := make([]int, 0, 3)

  if t.a > 0 {
    res = append(res, t.a)
  }
  if t.b > 0 {
    res = append(res, t.b)
  }
  if t.c > 0 {
    res = append(res, t.c)
  }

  return res
}

func getBiggestThree(grid [][]int) []int {
	m, n := len(grid), len(grid[0])
	p := (min(n, m) + 1) / 2 // max rhombus side length

  acc := &TopThree{}

  // iterate rhombus width from max (2p - 1) to min (1) exclusive
  for w := 2 * p - 1; w > 1; w -= 2 {
    
    // iterate rows x cols
    for r := range m - w + 1 {
      for c := range n - w + 1 {
        
        sum := 0 // rhombus sum

        // start left corner
        i, j := r + w / 2, c
        // go to the top corner
        for k := range w / 2 {
          sum += grid[i - k][j + k]
        }

        // start top
        i, j = r, c + w / 2
        // go to the right corner
        for k := range w / 2 {
          sum += grid[i + k][j + k]
        }

        // start right
        i, j = r + w / 2, c + w - 1
        // go to the bottom corner
        for k := range w / 2 {
          sum += grid[i + k][j - k]
        }

        // start bottom
        i, j = r + w - 1, c + w / 2
        // go to the left corner
        for k := range w / 2 {
          sum += grid[i - k][j - k]
        }

        acc.Put(sum)
      }
    }
  }

  // corner case (only cells)
  for i := range grid {
    for j := range grid[i] {
      acc.Put(grid[i][j])
    }
  }

  return acc.Get()
}