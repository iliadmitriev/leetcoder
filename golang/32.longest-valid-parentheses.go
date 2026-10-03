func longestValidParentheses(s string) int {

	scan := func(seq iter.Seq2[int, byte], ch byte) int {
		res := 0
		opening, closing := 0, 0
		for _, it := range seq {
			if it == ch {
				opening++
			} else {
				closing++
			}

			if opening == closing {
				res = max(res, opening+closing)
			}

			if closing > opening {
				opening, closing = 0, 0
			}
		}

		return res
	}

	return max(
		scan(slices.All([]byte(s)), '('),
		scan(slices.Backward([]byte(s)), ')'),
	)
}