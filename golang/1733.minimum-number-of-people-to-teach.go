func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	m := len(languages)             // number of users
	disconnected := make([]bool, m) // disconnected users
	common := make([]int, n+1)      // number of common languages of disconnected users
	totalDisconnected := 0          // total number of disconnected users

	// sort languages for each user
	for _, lang := range languages {
		sort.Ints(lang)
	}

	// check if two ordered slices share the same element
	// to determine if two users are connected with same language
	any := func(a, b []int) bool {
		n, m := len(a), len(b)
		for i, j := 0, 0; i < n && j < m; {
			if a[i] < b[j] {
				i++
			} else if a[i] > b[j] {
				j++
			} else {
				return true
			}
		}
		return false
	}

	for _, friend := range friendships {
		a, b := friend[0]-1, friend[1]-1

		// if users a and b are not connected then skip them
		if any(languages[a], languages[b]) {
			continue
		}

		disconnected[a], disconnected[b] = true, true
	}

	for user, disconnect := range disconnected {
		if !disconnect {
			continue
		}

		totalDisconnected++
		for _, lang := range languages[user] {
			common[lang]++
		}
	}

	return totalDisconnected - slices.Max(common)
}
