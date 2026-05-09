func predictPartyVictory(senate string) string {
    que := make([]rune, len(senate))
    r, d, ban_r, ban_d := 0, 0, 0, 0

    for _, i := range senate {
        que = append(que, i)
        if i == 'R' {
            r++
        } else {
            d++
        }
    }

    for len(que) > 0 {
        sen := que[0] 
        que = que[1:]

        if sen == 'R' && r > 0 {
            if ban_r > 0 {
                ban_r--
                continue
            }

            if d > 0 {
                d--
                ban_d++
                que = append(que, sen)
                continue
            }

            return "Radiant"

        } else if sen == 'D' && d > 0 {
            if ban_d > 0 {
                ban_d--
                continue
            }

            if r > 0 {
                r--
                ban_r++
                que = append(que, sen)
                continue
            }

            return "Dire"
        }
    }

    if ban_r == 0 && r > 0 {
        return "Radiant"
    }
    return "Dire"
}