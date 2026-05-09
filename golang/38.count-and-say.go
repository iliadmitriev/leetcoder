func countAndSay(n int) string {
	res := "1"

	for n--; n > 0; n-- {
		tmp := strings.Builder{}

		for i := 0; i < len(res); {
			cur := res[i]
			cnt := 0
			for i < len(res) && cur == res[i] {
				cnt++
				i++
			}

			tmp.WriteString(strconv.Itoa(cnt))
			tmp.WriteByte(cur)
		}

		res = tmp.String()
	}

	return res
}
