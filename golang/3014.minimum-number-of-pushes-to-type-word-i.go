func minimumPushes(word string) int {
    const N = 26

    cnt := make([]int, N)
    count := 0
    step := 0

    for _, ch := range word {
      cnt[ch - 'a']++
    }

    slices.Sort(cnt)

    for i := N - 1; i >= 0 && cnt[i] > 0; i-- {
      if (N - i - 1) % 8 == 0 {
        step++
      }

      count += step * cnt[i]
    }

    return count
}