type Key struct{
    a, b int
}

// i - current pos
// k - current speed
func dpCanCross(i int, k int, last int, stoneSet map[int]bool, dpCache map[Key]bool) bool {
    // if speed reduces to 0 and lower
    if k <= 0 { return false }

    // if encountered final last stone
    if i == last { return true }

    // check if this move is even possible
    if _, ok := stoneSet[i + k]; !ok { return false }

    // check if value for i was calculated already
    if val, ok := dpCache[Key{i, k}]; ok { return val }

    res := false

    for _, step := range []int{-1, 0, 1} {
        if ( dpCanCross(i + k, k + step, last, stoneSet, dpCache) ) {
            res = true
            break
        }
    }

    // cache and return result
    dpCache[Key{i, k}] = res
    return res
}

func canCross(stones []int) bool {
    stoneSet  := make(map[int]bool)
    dpCache   := make(map[Key]bool)

    last := stones[len(stones) - 1]

    for _, stone := range(stones) { stoneSet[stone] = true }

    return dpCanCross(0, 1, last, stoneSet, dpCache)
}