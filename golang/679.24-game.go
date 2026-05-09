
const EPS = 1e-6

func judgePoint24(cards []int) bool {
	fcards := make([]float64, len(cards))
	for i, card := range cards {
		fcards[i] = float64(card)
	}

	return dfsJudge(fcards)
}

func dfsJudge(cards []float64) bool {
	if len(cards) == 1 {
		return math.Abs(cards[0]-24.0) < EPS
	}

	for i := range len(cards) - 1 {
		for j := i + 1; j < len(cards); j++ {
			newCards := make([]float64, 0, 4)
			for k, c := range cards {
				if k != i && k != j {
					newCards = append(newCards, c)
				}
			}

			ops := make([]float64, 0, 4+2+1)
			ops = append(ops,
				cards[i]+cards[j],
				cards[i]*cards[j],
				cards[i]-cards[j],
				cards[j]-cards[i],
			)

			if cards[i] > EPS {
				ops = append(ops, cards[j]/cards[i])
			}

			if cards[j] > EPS {
				ops = append(ops, cards[i]/cards[j])
			}

			for _, op := range ops {
				if dfsJudge(append(newCards, op)) {
					return true
				}
			}
		}
	}

	return false
}
