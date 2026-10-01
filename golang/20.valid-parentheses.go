func isValid(s string) bool {
	st := []rune{}

	for _, ch := range s {
		switch ch {
		case '(', '{', '[':
			{
				st = append(st, ch)
			}
		case ')':
			{
				if len(st) == 0 || st[len(st)-1] != '(' {
					return false
				}
				st = st[:len(st)-1]
			}
		case '}':
			{
				if len(st) == 0 || st[len(st)-1] != '{' {
					return false
				}
				st = st[:len(st)-1]
			}
		case ']':
			{
				if len(st) == 0 || st[len(st)-1] != '[' {
					return false
				}
				st = st[:len(st)-1]
			}
		default:
			return false
		}
	}

	return len(st) == 0
}