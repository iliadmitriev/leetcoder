func findRestaurant(list1 []string, list2 []string) []string {
	m, n := len(list1), len(list2)
	hash1 := make(map[string]int, m)

	for i := range list1 {
		hash1[list1[i]] = i
	}

	res := []string{}
	minVal := m + n

	for i := range list2 {
		if v, ok := hash1[list2[i]]; ok {
			if v+i < minVal {
				minVal = v + i
				res = []string{list2[i]}
			} else if v+i == minVal {
				res = append(res, list2[i])
			}
		}
	}

	return res
}
