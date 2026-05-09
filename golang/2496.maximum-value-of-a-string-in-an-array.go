func maximumValue(strs []string) int {
	maxStr := 0

	for i := range strs {
		lenStr, err := strconv.Atoi(strs[i])
		if err != nil {
			lenStr = len(strs[i])
		}

		if lenStr > maxStr {
			maxStr = lenStr
		}
	}

	return maxStr
}
