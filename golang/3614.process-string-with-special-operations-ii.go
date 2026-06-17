func processStr(s string, k int64) byte {
	var size int64

	for i := range len(s) {
		ch := s[i]

		switch ch {
		case '*': // delete
			size = max(0, size-1)
		case '#': // double
			size *= 2
		case '%':
			// reverse (length doesn't change)
		default:
			size++ // symbol
		}
	}

	if k >= size {
		return '.'
	}

	// backwards
	for i := len(s) - 1; i >= 0; i-- {
		ch := s[i]

		switch ch {
		case '*': // reverse delete
			size++
		case '#': // reverse double
			half := size / 2

			if k >= half { // index change only if second half
				k -= half
			}

			size = half
		case '%': // reverse revese (indexation)
			k = size - 1 - k
		default: // reverse symbol adding
			if k == size-1 {
				return ch // current symbol is k-th
			}

			size-- // remove
		}
	}

	return '.' // default
}