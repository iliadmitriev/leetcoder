func countTestedDevices(batteryPercentages []int) int {
	devices := 0

	for _, charge := range batteryPercentages {
		if charge > devices {
			devices++
		}
	}

	return devices
}
