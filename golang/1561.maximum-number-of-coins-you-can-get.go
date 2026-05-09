func maxCoins(piles []int) int {

    res := 0
    
    freq := make(map[int]int)
    top := 0
    for _, p := range piles {
        freq[p]++
        if p > top {
            top = p
        }
    }

    for n := len(piles) / 3; n > 0; n-- {

        // get next top pile value
        for (top > 0 && freq[top] == 0) {
            top--
        }
        // and remove it from the pile
        freq[top]--

        for (top > 0 && freq[top] == 0) {
            top--
        }
        freq[top]--

        res += top        
    }

    return res
}
