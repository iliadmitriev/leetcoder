import (
    "strings"
)

func calculate(s string) int {
    
    op := byte('+')
    s += "+"

    res := 0
	num := 0
    last := 0

	for i := range s {
		v := s[i]

		if '0' <= v && v <= '9' {
			num = num*10 + int(v-'0')
		} else if v == '+' || v == '-' || v == '/' || v == '*' {
			if op == '-' {
                res += last
                last = -num
			} else if op == '+' {
                res += last
                last = num
			} else if op == '/' {
				last /= num
			} else if op == '*' {
				last *= num
			}

			num = 0
            op = v
		}

	}

	return res + last
}