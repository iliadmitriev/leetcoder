func findLongestChain(pairs [][]int) int {

    sort.Slice(pairs, func(i int, j int) bool {
        return pairs[i][1] < pairs[j][1]
    })
    length := 1
    end := pairs[0][1]

    for _, pair := range pairs {
        if end < pair[0] {
            end = pair[1]
            length++
        }
    }

    return length
    
}