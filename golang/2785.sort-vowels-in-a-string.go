type Tuple struct {
    ch rune
    v int
}

func sortVowels(s string) string {
    t := []rune(s)
    w := map[rune]int{'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for _, ch := range t {
        if _, ok := w[ch]; ok {
            w[ch]++
        }
    }

    buffer := make([]Tuple, 0, len(w))
    for k, v := range w {
        if v > 0 {
            buffer = append(buffer, Tuple{k, v})
        }
    }
    sort.Slice(buffer, func (i,j int) bool {
        return buffer[i].ch < buffer[j].ch
    })
    
    for i, ch := range t {
        if _, ok := w[ch]; !ok {
           continue
        }

        if buffer[0].v == 0 {
            buffer = buffer[1:]
        }

        t[i] = buffer[0].ch
        buffer[0].v--

    }

    return string(t)

}