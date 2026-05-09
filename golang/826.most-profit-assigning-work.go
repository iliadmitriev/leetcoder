func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	jobs := make([][2]int, len(difficulty))
	for i := range jobs {
		jobs[i] = [2]int{difficulty[i], profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool {
		if jobs[i][0] != jobs[j][0] {
			return jobs[i][0] < jobs[j][0]
		}

		return jobs[i][1] < jobs[j][1]
	})

	sort.Ints(worker)
	maxProfit := 0
	bestJob := 0
	i := 0

	for _, w := range worker {
		for i < len(jobs) && jobs[i][0] <= w {
			bestJob = max(bestJob, jobs[i][1])
			i++
		}

		maxProfit += bestJob
	}

	return maxProfit
}
