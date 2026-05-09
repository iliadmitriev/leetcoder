// [23,2,4,6,7] k = 6
// reminder set {5, 1, 5, 0}
// [5, 1, 5, 5, 0]
// [[23,6,9]] 6
// 5, 5

func checkSubarraySum(nums []int, k int) bool {
    cache := map[int]int{0: 0}
    prefix := 0

    for i, num := range nums {
      prefix += num
      prefix %= k

      if _, ok := cache[prefix]; !ok {
        cache[prefix] = i + 1
      } else if cache[prefix] < i {
        return true
      }

    }

    return false
}