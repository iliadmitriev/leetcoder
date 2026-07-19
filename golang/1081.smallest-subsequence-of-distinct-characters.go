func smallestSubsequence(s string) string {
    top := -1
    st := make([]byte, 26) // stack and it's top

    added := make([]bool, 26) // characters already added on the stack
    cnt := make([]uint32, 26) // number of characters left

    // all the characters available for deletion at the start
    for i := 0; i < len(s); i++ {
      cnt[s[i] - 'a']++
    }

    for i := 0; i < len(s); i++ {
      p, ch := s[i] - 'a', s[i]

      // reduce the number of characters left
      cnt[p]--

      // check if current character on the stack and skip it
      if added[p] {
        continue
      }

      // if current character is lexicographically smaller then
      // the character on the top of the stack
      // and can be replaced (still have replacements left)
      // then drop it
      for top != -1 && ch < st[top] && cnt[st[top] - 'a'] > 0 {
        added[st[top] - 'a'] = false // drop
        top--
      }

      // add character on the stack
      top++
      st[top] = ch
      added[p] = true
    }

    return string(st[:top+1])
}