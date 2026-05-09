/*

[[4,0,2,0],
 [0,3,0,1],
 [2,0,2,0],
 [0,1,0,1]]

w: [a,b,a,b]

(diagonality)
[[4,3,2,1],
 [3,3,2,1],
 [2,2,2,1],
 [1,1,1,1]]

*/

type UF struct {
  p []int
}

func NewUF(n int) *UF {
  p := make([]int, n)
  for i := range p {
    p[i] = i
  }

  return &UF{p: p}
}

func (u *UF) find(x int) int {
  for x != u.p[x] {
    u.p[x] = u.p[u.p[x]]
    x = u.p[x]
  }

  return x
}

func (u *UF) join(x, y int) bool {
  px, py := u.find(x), u.find(y)
  if px == py {
    return false
  }

  u.p[py] = px

  return true
}

func findTheString(lcp [][]int) string {
	n := len(lcp)
  uf := NewUF(n)
  ch := make([]byte, n) // colors (for components)
	word := make([]byte, n)
  cur := byte('a')

  // 1. check if lcp matrix is valid and diagonal
  for i := range n {
    if lcp[i][i] != n - i {
      return "" // matrix main diaginal is not valid, it should be [...4,3,2,1]
    }

    for j := range n {
      if lcp[i][j] != lcp[j][i] {
        return "" // matrix doesn't have diagonal symmetry
      }
    }
  }

  // 2. union find all cells that has common prefix
  for i := range n {
    for j := range n {
      if lcp[i][j] > 0 {
        uf.join(i, j)
      }
    }
  }

  // 3. construct word candidate (greedy assign smallest possible char)
  for x := range n {
    px := uf.find(x) // px - found component for vertice x

    if ch[px] == 0 { // color for component is not set
      if cur > 'z' {
        return "" // there is no letters (colors) left
      }
      // set next lexicograpihcal symbol to component
      ch[px] = cur
      cur++
    }

    word[x] = ch[px] // color this component
  } 


	// 4. check if constructed word candidate matches LCP matrix requirements
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if word[i] != word[j] { // if word prefixes don't match
				if lcp[i][j] != 0 { // but LCP matrix prefixes matches (contradiction)
					return "" // impossible to match requirements
				}
			} else { // if word prefixes match
				if i == n-1 || j == n-1 {
					if lcp[i][j] != 1 { // start of the sequence begins with 1
						return ""
					}

				} else {
					if lcp[i][j] != lcp[i+1][j+1]+1 { // continue of the sequence previous length + 1
						return ""
					}
				}
			}
		}
	}

	return string(word)
}