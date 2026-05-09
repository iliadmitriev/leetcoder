func maxDistance(nums1 []int, nums2 []int) int {
    bisectRight := func(arr[]int, x, lo int) int {
      hi := len(arr)
      var mid, res int

      for lo < hi {
        mid = (lo + hi) / 2

        // [100,20,10,10,5] >= 55
        if arr[mid] >= x {
          lo = mid + 1
          res = mid
        } else {
          hi = mid
        }
      }

      return res
    }


    var maxDist int

    for i, num := range nums1 {
      j := bisectRight(nums2, num, i)
      maxDist = max(maxDist, j - i)
    }

    return maxDist
}