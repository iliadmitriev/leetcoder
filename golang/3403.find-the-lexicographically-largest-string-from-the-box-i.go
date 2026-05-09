func answerString(word string, numFriends int) string {
	if numFriends == 1 {
		return word
	}

	n := len(word)
	win := n - numFriends + 1
	i, j, k := 0, 1, 0

	for j+k < n {
		if word[i+k] == word[j+k] {
			k++
		} else if word[i+k] > word[j+k] {
			j = j + k + 1
			k = 0
		} else {
			i = i + k + 1
			j = i + 1
			k = 0
		}
	}

	return word[i:min(i+win, n)]
}
