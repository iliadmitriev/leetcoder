// Get words than fit into the line of maxWidth starting from the i-th word.
func getWords(i int, words []string, maxWidth int) []string {
    result := make([]string, 0)
    currentLen := 0

    for ; i < len(words) && currentLen + len(words[i]) <= maxWidth; i++ {
        result = append(result, words[i])
        currentLen += len(words[i]) + 1
    }
    return result
}

// Build line of text width justified from slice of words
// for a given i-th line
func buildJustifiedLine(line []string, i int, words []string, maxWidth int) string {
    baseWidth := -1
    for _, word := range line {
        baseWidth += len(word) + 1
    }

    extraSpaces := maxWidth - baseWidth

    if i == len(words) || len(line) == 1 {
        return strings.Join(line, " ") + strings.Repeat(" ", extraSpaces)
    }

    delimitersCount := len(line) - 1 // number of separations needed to split n words
    numberOfSpacesPerWord := extraSpaces / delimitersCount
    wordsNeededExtaSpaces := extraSpaces % delimitersCount

    for j := 0; j < wordsNeededExtaSpaces; j++ {
        line[j] += " "
    }

    delimiter := strings.Repeat(" ", numberOfSpacesPerWord)
    for j := 0; j < delimitersCount; j++ {
        line[j] += delimiter
    }

    return strings.Join(line, " ")
}

func fullJustify(words []string, maxWidth int) []string {
    res := make([]string, 0)
    i := 0

    for i < len(words) {
        currLine := getWords(i, words, maxWidth)
        i += len(currLine)
        res = append(res, buildJustifiedLine(currLine, i, words, maxWidth))
    }

    return res
}