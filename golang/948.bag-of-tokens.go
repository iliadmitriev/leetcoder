func bagOfTokensScore(tokens []int, power int) int {
    score := 0
    left, right := 0, len(tokens) - 1

    sort.Ints(tokens)

    for left <= right {
        if power >= tokens[left] {
            power -= tokens[left]
            left++
            score++
        } else if score > 0 && left + 1 < right {
            power += tokens[right]
            right--
            score--
        } else {
            break
        }
    }

    return score
}