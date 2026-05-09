func countOfAtoms(formula string) string {
	st := []map[string]int{{}}

	tokenizeFormula(formula, func(tok string) {
		if tok == "(" {
			st = append(st, map[string]int{})
		} else if tok == ")" {
			cur := flatten(&st)
			st = append(st, cur)
		} else if unicode.IsLetter(rune(tok[0])) {
			st = append(st, map[string]int{tok: 1})
		} else if unicode.IsDigit(rune(tok[0])) {
			cnt, _ := strconv.Atoi(tok)
			cur := st[len(st)-1]
			for k, v := range cur {
				cur[k] = v * cnt
			}
		}
	})

	res := flatten(&st)
	keys := make([]string, 0, len(res))
	for k := range res {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	out := make([]string, 0, len(keys)*2)
	for _, k := range keys {
		out = append(out, k)
		if res[k] > 1 {
			out = append(out, strconv.Itoa(res[k]))
		}
	}

	return strings.Join(out, "")
}

func flatten(stack *[]map[string]int) map[string]int {
	st := *stack
	m := map[string]int{}
	for len(st) > 0 && len(st[len(st)-1]) > 0 {
		s := st[len(st)-1]
		for k, v := range s {
			m[k] += v
		}
		st = st[:len(st)-1]
	}

	if len(st) > 0 && len(st[len(st)-1]) == 0 {
		st = st[:len(st)-1]
	}
	*stack = st

	return m
}

func tokenizeFormula(formula string, f func(string)) {
	for i := 0; i < len(formula); i++ {
		if formula[i] == '(' {
			f(formula[i : i+1])
		} else if formula[i] == ')' {
			f(formula[i : i+1])
		} else if unicode.IsLetter(rune(formula[i])) {
			j := i + 1
			for ; j < len(formula) && unicode.IsLower(rune(formula[j])); j++ {
			}
			f(formula[i:j])
			i = j - 1
		} else if unicode.IsDigit(rune(formula[i])) {
			j := i + 1
			for ; j < len(formula) && unicode.IsDigit(rune(formula[j])); j++ {
			}
			f(formula[i:j])
			i = j - 1
		}
	}
}
