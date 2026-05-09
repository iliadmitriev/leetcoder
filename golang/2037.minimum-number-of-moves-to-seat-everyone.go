
import "sort"

func minMovesToSeat(seats []int, students []int) int {
	sort.Ints(seats)
	sort.Ints(students)

	minMoves := 0

	for i := 0; i < len(seats); i++ {
		if seats[i] > students[i] {
			minMoves += seats[i] - students[i]
		} else {
			minMoves += students[i] - seats[i]
		}
	}

	return minMoves
}
