func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	satisfiedNotGrumpy := 0
	satisfiedGrumpyWindow := 0
	maxSatisfiedGrumpy := 0

	for i := 0; i < len(customers); i++ {
		satisfiedNotGrumpy += customers[i] * (1 - grumpy[i])

		satisfiedGrumpyWindow += customers[i] * grumpy[i]
		if i >= minutes {
			satisfiedGrumpyWindow -= customers[i-minutes] * grumpy[i-minutes]
		}

		maxSatisfiedGrumpy = max(maxSatisfiedGrumpy, satisfiedGrumpyWindow)
	}

	return satisfiedNotGrumpy + maxSatisfiedGrumpy
}
