import (
	"math/bits"
)

func sortByBits(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		// |--- ones count --| |----- bits ------|
		// 0000 0000 0000 0110 0000 0001 1010 1011
		a := bits.OnesCount(uint(arr[i]))<<16 | arr[i]
		b := bits.OnesCount(uint(arr[j]))<<16 | arr[j]
		return a < b
	})

	return arr
}