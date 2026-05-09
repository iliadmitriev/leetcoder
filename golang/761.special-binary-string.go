func makeLargestSpecial(s string) string {
	res := make([]string, 0)
	n := len(s)
  c := 0

	for i, j := 0, 0; j < n; j++ {
    if s[j] == '1' {
      c++
    } else {
      c--
    }

    if c == 0 {
      mid := makeLargestSpecial(s[i + 1:j])
      res = append(res, fmt.Sprintf("1%s0", mid))
      i = j + 1
    }
	}

  sort.Sort(sort.Reverse(sort.StringSlice(res)))

  return strings.Join(res, "")
}