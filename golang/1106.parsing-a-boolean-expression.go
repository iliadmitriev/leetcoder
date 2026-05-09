func parseBoolExpr(expression string) bool {
	stack := []byte{}
	op := byte(0)

	for i := 0; i < len(expression); i++ {
		tok := expression[i]

		if tok == ',' {
			continue
		}

		if tok == '!' || tok == '&' || tok == '|' {
			stack = append(stack, op)
			op = tok
		} else if expression[i] == '(' {
			continue
		} else if expression[i] == ')' {
			res := eval(&stack, op)
			op = stack[len(stack)-1]
			stack[len(stack)-1] = res
		} else {
			stack = append(stack, tok)
		}

	}

	return stack[len(stack)-1] == 't'
}

func eval(stack *[]byte, op byte) byte {
	st := *stack
	var res byte

	if op == '!' {
		top := st[len(st)-1]
		st = st[:len(st)-1]

		if top == 't' {
			res = 'f'
		} else {
			res = 't'
		}
	} else if op == '&' {
		res = 't'
		for len(st) > 0 && (st[len(st)-1] == 't' || st[len(st)-1] == 'f') {
			top := st[len(st)-1]
			st = st[:len(st)-1]

			if top == 'f' {
				res = 'f'
			}
		}
	} else if op == '|' {
		res = 'f'
		for len(st) > 0 && (st[len(st)-1] == 't' || st[len(st)-1] == 'f') {
			top := st[len(st)-1]
			st = st[:len(st)-1]

			if top == 't' {
				res = 't'
			}
		}
	}

	*stack = st
	return res
}
