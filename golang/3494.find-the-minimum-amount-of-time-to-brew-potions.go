func minTime(skill []int, mana []int) int64 {
	n := len(skill)          // producers (workers)
	m := len(mana)           // jobs (work amount)
	starts := make([]int, n) // worker starting time in the pipeline
	ends := make([]int, n)   // worker ending time in the pipeline

	globalShit := 0

	ends[0] = skill[0]
	for j := range n - 1 {
		starts[j+1] += starts[j] + skill[j]
		ends[j+1] += ends[j] + skill[j+1]
	}

	// iterate over jobs pairwise
	for i := range m - 1 {
		curr, prev := mana[i+1], mana[i]

		// discover max time shift as difference between previous work ending time
		// and current work starting time
		shift := 0
		for j := range n {
			shift = max(shift, prev*ends[j]-curr*starts[j])
		}

		globalShit += shift
	}

	return int64(globalShit + ends[n-1]*mana[m-1])
}
