func lemonadeChange(bills []int) bool {
	collected := make(map[int]int)
	const price = 5
	changeNotes := []int{10, 5}

	for _, bill := range bills {
		collected[bill]++

		if bill == price {
			continue
		}

		change := bill - price
		for _, note := range changeNotes {
			if change >= note && collected[note] > 0 {
				numNotes := min(change/note, collected[note])
				collected[note] -= numNotes
				change -= note * numNotes
			}
		}

		if change > 0 {
			return false
		}
	}

	return true
}
