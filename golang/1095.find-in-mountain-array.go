/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * type MountainArray struct {
 * }
 *
 * func (this *MountainArray) get(index int) int {}
 * func (this *MountainArray) length() int {}
 */
func bsearch(lo int, hi int, cond func(int) bool) int {
    var mid int
    for lo < hi {
        mid = (lo + hi) / 2
        if cond(mid) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func findInMountainArray(target int, mountainArr *MountainArray) int {
    _cache := make(map[int]int)
    _get := func(key int) int {
        if value, ok := _cache[key]; ok {
            return value
        }
        _cache[key] = mountainArr.get(key)
        return _cache[key]
    }

    // find peak
    length := mountainArr.length()
    peak := bsearch(1, length - 2, func(i int) bool {
        return _get(i) < _get(i + 1)
    })

    // find min in left part
    left := bsearch(0, peak, func(i int) bool {
        return _get(i) < target
    })
    if _get(left) == target {
        return left
    }


    // find min in right part
    right := bsearch(peak + 1, length - 1, func(i int) bool {
        return _get(i) > target
    })
    if _get(right) == target {
        return right
    }

    return -1
}