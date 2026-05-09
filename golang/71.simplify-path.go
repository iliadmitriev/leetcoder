func simplifyPath(path string) string {
	n := len(path)
  st := [][2]int{}

  j := 0
  i := 0
	for j < n && i < n {
    if path[i] != '/' {
      i++
      continue
    }

		switch path[j: i] {
    case ".", "":
		case "..":
			k := len(st) - 1
			if k >= 0 {
				st = st[:k]
			}
		default:
			st = append(st, [2]int{j, i})
		}

    i++
    j = i
	}

  if i > j {
		switch path[j: i] {
    case ".", "":
		case "..":
			k := len(st) - 1
			if k >= 0 {
				st = st[:k]
			}
		default:
			st = append(st, [2]int{j, i})
		}
  }

  res := strings.Builder{}
  res.WriteByte('/')

  m := len(st)
  for _, p := range st {
    res.WriteString(path[p[0]: p[1]])
    res.WriteByte('/')
  }

  s := res.String()
  if m > 0 {
    s = s[:len(s) - 1]
  }

  return s
}