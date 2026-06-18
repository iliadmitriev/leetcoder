func angleClock(hour int, minutes int) float64 {
	const (
		oneHour       = 30.0  // degrees in full our (360 / 12)
		oneMinute     = 6.0   // degrees in full minute (360 / 60)
		oneHourMinute = 0.5   // degrees in in minute per hour (360 / 12 / 60)
		half          = 180.0 // degrees in half circle (360 / 2)
		hours         = 12    // total hour
	)

	hour %= hours

	minutesDegree := float64(minutes) * oneMinute
	hoursDegree := float64(hour)*oneHour + float64(minutes)*oneHourMinute

	angle := minutesDegree - hoursDegree
	if angle < 0 {
		angle = -angle
	}

	if angle > half {
		angle = 2*half - angle
	}

	return angle
}