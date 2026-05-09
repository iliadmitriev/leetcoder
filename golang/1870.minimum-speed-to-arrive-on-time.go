func minSpeedOnTime(dist []int, hour float64) int {

	const mx int = 1e7
	x := sort.Search(mx, func(s int) bool {
        s++
        t := 0.0
	    for _, d := range dist {
		    t = math.Ceil(t)
		    t += float64(d) / float64(s)
	    }
	    return t <= hour
	})
	if x == mx {
		return -1
	}
	return x + 1
}