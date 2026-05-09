func binSearchLeft(arr []State, end int) int {
    lo, hi := 0, len(arr)
    var mid int

    for lo < hi {
        mid = (lo + hi) / 2
        if arr[mid].end < end {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

type Job struct {
    start int
    end int
    profit int
}

type State struct {
    end int
    maxProfit int
}

func jobScheduling(startTime []int, endTime []int, profit []int) int {
    jobs := make([]Job, 0, len(endTime))
    for i := range startTime { jobs = append(jobs, Job{startTime[i], endTime[i], profit[i]}) }

    sort.Slice(jobs, func(i, j int) bool {
        return jobs[i].end < jobs[j].end
    })

    // dp with state (ending time, max profit for the ending time)
    dp := make([]State, 0, len(jobs))
    dp = append(dp, State{0, 0})

    for _, job := range jobs {
        i := binSearchLeft(dp, job.start + 1) - 1

        currProfit := dp[i].maxProfit + job.profit
        if currProfit > dp[len(dp) - 1].maxProfit {
            dp = append(dp, State{job.end, currProfit})
        }
    }

    return dp[len(dp) - 1].maxProfit
}