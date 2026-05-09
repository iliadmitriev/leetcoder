/*

non inclusive window: A[mid] - A[mid + k]

Cases:

1: - x ---  A[mid] ------ A[mid + k] -- window is on the right, move left

2: -- A[mid] ------ A[mid + k] -- x --- window is on the left, move right

3: -- A[mid] -- x -------- A[mid + k] - window is in the middle, but left border is closer to x or draw, move left

4: -- A[mid] --------- x - A[mid + k] - window is in the middle, but right border is closer to x, move right

move left: shift hi, reduce mid
move right: shift lo, increase mid

*/

func findClosestElements(arr []int, k int, x int) []int {
    lo, hi := 0, len(arr) - k

    abs := func (x int) int {
        if x < 0 {
            return -x
        }
        return x
    }

    var mid int

    for lo < hi {
        mid = (lo + hi) / 2

        if x <= arr[mid] { // 1
            hi = mid
        } else if arr[mid + k] <= x { // 2
            lo = mid + 1
        } else if abs(x - arr[mid]) > abs(x - arr[mid + k]) { // 4
            lo = mid + 1
        } else { // 3
            hi = mid
        }
    }


    return arr[lo: lo + k]
}