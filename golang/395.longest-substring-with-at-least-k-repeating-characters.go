func longestSubstring(s string, k int) int {
  
	if len(s) < k {
		return 0
	}

  fmt.Println(s)
  
	n := len(s)
	cnt := map[byte]int{}
	div := map[byte]bool{}

	for i := range n {
		cnt[s[i]]++
	}

	for ch, v := range cnt {
		if v < k {
			div[ch] = true
		}
	}

	if len(div) == 0 {
		return len(s)
	}

	j := 0
  longest := 0

	for i := range n + 1 {
		if i == n || div[s[i]] {
			longest = max(longest, longestSubstring(s[j:i], k))
			j = i + 1
		}
	}

	return longest
}