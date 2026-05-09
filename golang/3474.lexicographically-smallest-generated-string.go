func generateString(str1 string, str2 string) string {
	n, m := len(str1), len(str2)
	s := make([]byte, n+m-1)
	fixed := make([]bool, n+m-1) // defautl all not fixed

	for i := range s {
		s[i] = 'a' // default all 'a'
	}

	for i := 0; i < n; i++ {
		if str1[i] == 'T' { // all pattern value should match for T
			for j := i; j < i+m; j++ {
				if fixed[j] && s[j] != str2[j-i] { // if found one value not matching
					return "" // return default
				} else {
					s[j] = str2[j-i] // set value
					fixed[j] = true  // fix value
				}
			}
		}
	}

	for i := 0; i < n; i++ {
		if str1[i] == 'F' { // any vlaue must be not equal to the pattern and lexicograpically smallest
			flag := false                     // not equal value is found
			idx := -1                         // first found index of not fixed value
			for j := i + m - 1; j >= i; j-- { // move backwards to meet lexicographically smallest
				if str2[j-i] != s[j] {
					flag = true // there is not equal value exists
				}
				if idx == -1 && !fixed[j] {
					idx = j // there is not fixed value
				}
			}
			if flag { // if there is a not equal value found
				continue // then nothing to do
			} else if idx != -1 { // next if pattern matches all values
				s[idx] = 'b' // mark it as next value 'b' (default is 'a')
			} else { // otherwise (equal to pattern and all values fixed)
				return "" // it's impossible to make any on values not equal as they all fixed
			}
		}
	}

	return string(s)
}