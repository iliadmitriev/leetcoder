func mapWordWeights(words []string, weights []int) string {
    res := make([]byte, len(words))

    worder := func(w string) byte {
      s := 0
      a := 'a'
      z := byte('z')

      for _, ch := range w {
        s += weights[ch - a]
      }
      
      return z - byte(s % 26)
    }

    for i, word := range words {
      res[i] = worder(word)
    }

    return string(res)
}