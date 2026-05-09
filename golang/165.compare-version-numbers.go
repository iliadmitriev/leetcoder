func compareVersion(version1 string, version2 string) int {
	i1, i2 := 0, 0
	d1, d2 := 0, 0
	for i1 < len(version1) || i2 < len(version2) {
		d1 = 0
		for ; i1 < len(version1) && version1[i1] != '.'; i1++ {
			d1 = d1*10 + int(version1[i1]-'0')
		}
		i1++

		d2 = 0
		for ; i2 < len(version2) && version2[i2] != '.'; i2++ {
			d2 = d2*10 + int(version2[i2]-'0')
		}
		i2++

		if d1 == d2 {
			continue
		} else if d1 > d2 {
			return 1
		} else {
			return -1
		}
	}

	return 0
}
