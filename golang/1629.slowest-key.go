func slowestKey(releaseTimes []int, keysPressed string) byte {

	prev := 0
	maxDuration := 0
	maxDurationKey := byte(0)

	for i := 0; i < len(releaseTimes); i++ {
		curr := releaseTimes[i]
		duration := curr - prev
		prev = curr

		if duration > maxDuration || (duration == maxDuration && keysPressed[i] > maxDurationKey) {
			maxDuration = duration
			maxDurationKey = keysPressed[i]
		}
	}

	return maxDurationKey

}
