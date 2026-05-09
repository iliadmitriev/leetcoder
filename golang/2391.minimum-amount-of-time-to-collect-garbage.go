func garbageCollection(garbage []string, travel []int) int {
    total := 0
    f, m, p, g := 0, 0, 0, 0
    _m, _p, _g := false, false, false

    for i, house := range garbage {
        total += len(house)

        if i > 0 {
            f += travel[i - 1]
        }

        _m, _p, _g = false, false, false
        for j := 0; j < len(house); j++ {
            if !_m && house[j] == 'M' {
                m = f
                _m = true
            }
            if !_p && house[j] == 'P' {
                p = f
                _p = true
            }
            if !_g && house[j] == 'G' {
                g = f
                _g = true
            }
            if _m && _g && _p {
                break
            }
        }
    }

    return total + m + p + g
}