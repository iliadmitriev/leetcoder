import "math"

func thirdMax(nums []int) int {
	const NEG_INF = math.MinInt

	L, M, S := NEG_INF, NEG_INF, NEG_INF

	for _, num := range nums {
		if num > L {
			S = M
			M = L
			L = num
		} else if num > M && num != L {
			S = M
			M = num
		} else if num > S && num != M && num != L {
			S = num
		}
	}

	if S == NEG_INF {
		return L
	}

	return S
}
