
func countOdds(low int, high int) int {
	// odd numbers between [0, x] inlusive is (x + 1) / 2
	// odd numbers between [0, x) exclusive is x / 2

	return (high+1)/2 - low/2
}
