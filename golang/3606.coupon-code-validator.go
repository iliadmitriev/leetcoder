
func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
	validBusiness := map[string]bool{
		"electronics": true, "grocery": true, "pharmacy": true, "restaurant": true,
	}

	filtered := make([][2]string, 0, len(code))
	isCodeValid := func(code string) bool {
		// code consist only of [A-Za-z0-9_]
		for _, ch := range code {
			if ('A' > ch || ch > 'Z') && ('a' > ch || ch > 'z') && ('0' > ch || ch > '9') && ch != '_' {
				return false
			}
		}

		return true
	}

	for i, codeID := range code {
		if !isActive[i] || !validBusiness[businessLine[i]] || len(codeID) == 0 {
			continue
		}

		if !isCodeValid(codeID) {
			continue
		}

		filtered = append(filtered, [2]string{businessLine[i], codeID})
	}

	sort.Slice(filtered, func(i, j int) bool {
		if filtered[i][0] == filtered[j][0] {
			return filtered[i][1] < filtered[j][1]
		}

		return filtered[i][0] < filtered[j][0]
	})

	result := make([]string, 0, len(filtered))
	for i := range filtered {
		result = append(result, filtered[i][1])
	}

	return result
}
