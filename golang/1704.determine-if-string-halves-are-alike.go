func halvesAreAlike(s string) bool {
    mid := len(s) / 2
    count := 0

    for i, ch := range s {
        switch ch {
            case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U': {
                if i < mid {
                    count ++
                } else {
                    count --
                }
            }
        }
    }

    return count == 0
}