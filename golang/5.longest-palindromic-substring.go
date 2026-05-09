func longestPalindrome(s string) string {
	n := len(s)
  longest := ""
  longestLen := 0

	for cen := 0; cen < n; cen++ {
    i, j := cen, cen
    //                     *
    // shift j if odd "...abba..."
    for j < n - 1 && s[i] == s[j + 1] {
      j++
      cen++
    }

    for i > 0 && j < n - 1 && s[i - 1] == s[j + 1] {
      i--
      j++
    }

    if longestLen < j - i + 1 {
      longestLen = j - i + 1
      longest = s[i: j + 1]
    }

	}

  return longest
}