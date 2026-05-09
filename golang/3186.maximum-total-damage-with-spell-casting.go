func maximumTotalDamage(power []int) int64 {
	cnt := make(map[int]int)
	for _, pwr := range power {
		cnt[pwr]++
	}

	powers := make([]int, 0, len(cnt))
	for pwr := range cnt {
		powers = append(powers, pwr)
	}

	slices.Sort(powers)

	dp, dp1, dp2, dp3 := 0, 0, 0, 0 // final resuls and 3 previuos maximum gained damage
	p1, p2 := 0, 0                  // previous used powers

	for _, pwr := range powers {
		value := pwr * cnt[pwr]

		dp = max(dp3+value, max(dp1, dp2))

		if pwr-p2 > 2 {
			dp = max(dp, dp2+value)
		}

		if pwr-p1 > 2 {
			dp = max(dp, dp1+value)
		}

		dp1, dp2, dp3 = dp, dp1, dp2
		p1, p2 = pwr, p1
	}

	return int64(dp)
}
