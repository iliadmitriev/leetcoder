func isIsomorphic(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    m1 := make(map[byte]byte)
    m2 := make(map[byte]byte)

    for i := range len(s) {
        c1 := s[i]
        c2 := t[i]

        if v2, ok1 := m1[c1]; ok1 {
            if v2 != c2 {
                return false
            }
        } else {
            m1[c1] = c2
        }

        if v1, ok2 := m2[c2]; ok2 {
            if v1 != c1 {
                return false
            }
        } else {
            m2[c2] = c1
        }
    }

    return true
}