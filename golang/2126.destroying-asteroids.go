func asteroidsDestroyed(mass int, asteroids []int) bool {
  heavy := 0

  for _, ast := range asteroids {
    if mass >= ast {
      mass += ast
    } else {
      asteroids[heavy] = ast
      heavy++
    }
  }

  slices.Sort(asteroids[:heavy])

	for _, ast := range asteroids[:heavy] {
		if mass < ast {
			return false
		}

		mass += ast
	}

	return true
}