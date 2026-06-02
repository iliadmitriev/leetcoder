import (
	"iter"
)

func Zip[T, U any](a []T, b []U) iter.Seq2[T, U] {
	return func(yield func(T, U) bool) {
		length := min(len(a), len(b))

		for i := range length {
			if !yield(a[i], b[i]) {
				return
			}
		}
	}
}

// T, U -> V
func Map[T, U, V any](seq iter.Seq2[T, U], transform func(T, U) V) iter.Seq[V] {
	return func(yield func(V) bool) {
		for t, u := range seq {
			if !yield(transform(t, u)) {
				return
			}
		}
	}
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	bestLand := slices.Min(
		slices.Collect(
			Map(
				Zip(landStartTime, landDuration),
				func(start, duration int) int {
					return start + duration
				},
			),
		),
	)

	bestWater := slices.Min(
		slices.Collect(
			Map(
				Zip(waterStartTime, waterDuration),
				func(start, duration int) int {
					return start + duration
				},
			),
		),
	)

  bestLandWater := slices.Min(
		slices.Collect(
			Map(
				Zip(waterStartTime, waterDuration),
				func(start, duration int) int {
					return max(start, bestLand) + duration
				},
			),
		),
	)

  bestWaterLand := slices.Min(
		slices.Collect(
			Map(
				Zip(landStartTime, landDuration),
				func(start, duration int) int {
					return max(start, bestWater) + duration
				},
			),
		),
	)

	return min(bestLandWater, bestWaterLand)
}