func nextGreatestLetter(letters []byte, target byte) byte {
    lo, hi := 0, len(letters)
    var mid int
    for lo < hi {
        mid = (lo + hi) / 2
        if letters[mid] <= target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }

    if lo == len(letters) {
        return letters[0]
    }
    return letters[lo]
}