func findMin(nums []int) int {

  var mid int
  lo, hi := 0, len(nums) - 1

  for lo < hi {
    mid = (lo + hi) / 2

    if nums[lo] <= nums[mid] && nums[mid] >= nums[hi] { // min is on the left
      lo = mid + 1
    } else {
      hi = mid
    }
  }

  return nums[lo]
}