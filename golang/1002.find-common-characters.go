
func count(word string) []int {
	res := make([]int, 26)

	for i := range word {
		res[word[i]-'a']++
	}
	return res
}

func commonChars(words []string) []string {
	res := count(words[0])

	for i := 1; i < len(words); i++ {
		tmp := count(words[i])
		for j := 0; j < 26; j++ {
			res[j] = min(res[j], tmp[j])
		}
	}

	out := make([]string, 0)
	for i, v := range res {
		for j := 0; j < v; j++ {
			out = append(out, string(i+'a'))
		}
	}

	return out
}
