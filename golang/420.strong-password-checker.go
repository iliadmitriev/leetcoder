func strongPasswordChecker(password string) int {
	missingTypes := countMissingTypes(password)
	deletions := max(0, len(password)-20)
	insertions := max(0, 6-len(password))
	charsRepetitions := countRepeatingChars(password)
	breakRepetionWithDeletion(charsRepetitions, deletions)
	numberOfBreaks := countNumberOfBreaks(charsRepetitions)

	return deletions + max(insertions, max(numberOfBreaks, missingTypes))
}

func countNumberOfBreaks(charsRepetitions []int) int {
	count := 0
	for _, lenChars := range charsRepetitions {
		if lenChars >= 3 {
			count += lenChars / 3
		}
	}

	return count
}

func getMinIdxWithLambda(values []int, cmp func(int, int) bool) int {
	idx := 0

	for i := 1; i < len(values); i++ {
		if cmp(values[i], values[idx]) {
			idx = i
		}
	}
	return idx
}

func cmpKey(a int) int {
	if a >= 3 {
		return a % 3
	} else {
		return math.MaxInt
	}
}

func breakRepetionWithDeletion(repeatingChars []int, deletions int) {
	for deletions > 0 {
		deleteIdx := getMinIdxWithLambda(repeatingChars, func(a, b int) bool {
			return cmpKey(a) < cmpKey(b)
		})
		repeatingChars[deleteIdx]--
		deletions--
	}
}

func countRepeatingChars(password string) []int {
	res := make([]int, 0, len(password))

	for i := 0; i < len(password); i++ {
		if i == 0 || password[i] != password[i-1] {
			res = append(res, 1)
		} else {
			res[len(res)-1]++
		}
	}
	return res
}

func countMissingTypes(password string) int {
	missingTypesLower, missingTypesUpper, missingTypesDigit := true, true, true
	for i := 0; i < len(password); i++ {
		if isLower(password[i]) {
			missingTypesUpper = false
		} else if isUpper(password[i]) {
			missingTypesLower = false
		} else if isDigit(password[i]) {
			missingTypesDigit = false
		}
	}

	missingTypes := 0
	if missingTypesLower {
		missingTypes++
	}
	if missingTypesUpper {
		missingTypes++
	}
	if missingTypesDigit {
		missingTypes++
	}

	return missingTypes
}

func isLower(char byte) bool {
	return char >= 'a' && char <= 'z'
}

func isUpper(char byte) bool {
	return char >= 'A' && char <= 'Z'
}

func isDigit(char byte) bool {
	return char >= '0' && char <= '9'
}
