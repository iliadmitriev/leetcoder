func minLength(s string) int {
    st := make([]byte, 0, len(s))
    var ch, top byte
    for i := 0; i < len(s); i++ {
        ch = s[i]

        if len(st) == 0 {
            st = append(st, ch)
            continue
        }

        top = st[len(st) - 1]
        
        if (top == 'A' && ch == 'B') || (top == 'C' && ch == 'D') {
            st = st[:len(st) - 1]
            continue
        }
        
        st = append(st, ch)
    }

    return len(st)
}