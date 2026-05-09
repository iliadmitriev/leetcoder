/*



array:
  [abcd dcba lls s sssll]
map:
  [dcba:0 abcd:1 sll:2 s:3 llsss:4]

abcd: abcd, abc, bcd 1,0
dcba: dcba, dcb, cba 0,1
lls: lls ll ls s 3,2
s: s -
sssll: sssll ssll sll sssl sss 2,4

*/
func palindromePairs(words []string) [][]int {
	n := len(words)
	rev := make(map[string]int, n) // map of reversed words to indexes (words uniq, so reversed also uniq)
	ans := make([][]int, 0)

	revs := func(s string) string {
		res := []byte(s)
		for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
			res[i], res[j] = res[j], res[i]
		}

		return string(res)
	}

	pal := func(s string) bool {
		for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
			if s[i] != s[j] {
				return false
			}
		}

		return true
	}

	for i, w := range words {
		rev[revs(w)] = i
	}

	for i, w := range words {
		// case 1: check if there is a mirrored counterpart of a word
		if j, ok := rev[w]; ok && i != j {
			ans = append(ans, []int{j, i})
		}

		// case 2: a string is a palindrome by itself so look for combination with ""
		if j, ok := rev[""]; ok && i != j && pal(w) {
			ans = append(ans, []int{j, i})
			ans = append(ans, []int{i, j})
		}

		// case 3: check if part of word is a palindrome and
		// theres is exists the rest of the word reversed
		for k := 1; k < len(w); k++ {
			prefix, suffix := w[k:], w[:k]

			if j, ok := rev[suffix]; ok && i != j && pal(prefix) {
				ans = append(ans, []int{i, j})
			}

			if j, ok := rev[prefix]; ok && i != j && pal(suffix) {
				ans = append(ans, []int{j, i})
			}
		}
	}

	return ans
}