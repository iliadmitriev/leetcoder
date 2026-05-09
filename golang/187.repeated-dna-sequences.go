func findRepeatedDnaSequences(s string) []string {
	const length = 10
	const base = 7

	if len(s) < length {
		return []string{}
	}

	dict := make([]int, 85)
	dict['A'], dict['C'], dict['G'], dict['T'] = 1, 2, 3, 4

	prefix, power := 0, 1

	res := make([]string, 0)
	doubles := make(map[int]int)
	n := len(s)

	for i := 0; i < n; i++ {
		prefix *= base
		prefix += dict[s[i]]

		if i < length {
			power *= base

			if i == length-1 {
				doubles[prefix]++
			}

			continue
		}

		prefix -= dict[s[i-length]] * power
		doubles[prefix]++

		if doubles[prefix] == 2 {
			res = append(res, s[i-length+1:i+1])
		}
	}

	return res
}
