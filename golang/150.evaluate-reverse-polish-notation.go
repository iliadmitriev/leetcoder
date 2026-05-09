import (
	"strconv"
)

func evalRPN(tokens []string) int {

	st := []int{} // stack of operands

	itoa := func(s string) int { x, _ := strconv.Atoi(s); return x }
	operators := map[string]func(int, int) int{
		"+": func(a, b int) int { return a + b },
		"-": func(a, b int) int { return a - b },
		"/": func(a, b int) int { return a / b },
		"*": func(a, b int) int { return a * b },
	}

	for _, token := range tokens {

		if op, ok := operators[token]; ok {
			n := len(st)
			a, b := st[n-2], st[n-1]
			st = append(st[:n-2], op(a, b))
		} else {
			st = append(st, itoa(token))
		}
	}

	return st[0]
}