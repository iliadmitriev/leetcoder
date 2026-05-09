import (
	"math"
)

func distributeCandies(candies int, num_people int) []int {
	res := make([]int, num_people)

	n := (int(math.Sqrt(float64(8*candies+1))) - 1) / 2 // total number of times candies given
	s := n * (n + 1) / 2                                // total candies given to all people
	r := n % num_people                                 // index of person who gets the last candy
	l := candies - s                                    // leftover candies

	for i := range num_people {
		n1 := n / num_people // number of times person i gets a candies
		if i < r {
			n1++
		}

		// sum of all candies given to person i
		// arithmetic progressiong with start i + 1, step num_people and last number n1
		s1 := n1 * (2*(i+1) + (n1-1)*num_people) / 2
		res[i] = s1
	}

	res[r] += l

	return res
}
