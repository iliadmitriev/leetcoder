import (
	"iter"
	"slices"
)

// Zip []T, []U -> [](T, U)
func Zip[T, U any](v1 []T, v2 []U) iter.Seq2[T, U] {
	return func(yield func(T, U) bool) {
		length := min(len(v1), len(v2))

		for i := range length {
			if !yield(v1[i], v2[i]) {
				return
			}
		}
	}
}

// Map [](T, U) -> []V
func Map[T, U, V any](seq iter.Seq2[T, U], transform func(a T, b U) V) iter.Seq[V] {
	return func(yield func(V) bool) {
		for t, u := range seq {
			if !yield(transform(t, u)) {
				return
			}
		}
	}
}

// Min []T -> T
func Min[T cmp.Ordered](seq iter.Seq[T]) T {
	return slices.Min(slices.Collect(seq))
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	bestLand := Min(Map(
		Zip(landStartTime, landDuration),
		func(s, e int) int {
			return s + e
		}))

	bestWater := Min(Map(
		Zip(waterStartTime, waterDuration),
		func(s, e int) int {
			return s + e
		}))

	bestLandWater := Min(Map(
		Zip(waterStartTime, waterDuration),
		func(s, e int) int {
			return max(bestLand, s) + e
		}))

	bestWaterLand := Min(Map(
		Zip(landStartTime, landDuration),
		func(s, e int) int {
			return max(bestWater, s) + e
		}))

	return min(bestLandWater, bestWaterLand)
}