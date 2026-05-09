func numberOfBeams(bank []string) int {
    beams := 0
    prev, cur := 0, 0
    counter := 0

    for r := 0; r < len(bank); r++ {
        counter = 0
        for i := 0; i < len(bank[r]); i++ {
            if bank[r][i] == '1' {
                counter++
            }
        }

        if counter > 0 {
            prev = cur
            cur = counter
            beams += prev * cur
        }
    }

    return beams
}