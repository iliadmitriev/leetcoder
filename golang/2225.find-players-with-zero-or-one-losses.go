func findWinners(matches [][]int) [][]int {
    scores := make(map[int]int)
    
    for _, match := range matches {
        winner, loser := match[0], match[1]
        
        if _, ok := scores[winner]; !ok {
            scores[winner] = 0
        }

        scores[loser]++
    }

    res_zero, res_one := make([]int, 0, len(scores) / 2), make([]int, 0, len(scores) / 2)
    for player, count := range scores {
        switch count {
            case 0: res_zero = append(res_zero, player)
            case 1: res_one = append(res_one, player)
        }
    }

    sort.Ints(res_zero)
    sort.Ints(res_one)

    return [][]int{res_zero, res_one}
}