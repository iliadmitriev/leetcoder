
import (
	"strconv"
)

var months = [13]int{0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334}

func dayOfYear(s string) int {
	m, d := s[0:2], s[3:5]
	mm, _ := strconv.Atoi(m)
	dd, _ := strconv.Atoi(d)

	return dd + months[mm]
}

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
    arrive := max(dayOfYear(arriveAlice), dayOfYear(arriveBob))
    leave := min(dayOfYear(leaveAlice), dayOfYear(leaveBob))
    
    return max(0, leave - arrive + 1)
}