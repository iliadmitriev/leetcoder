/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
    lo, hi := 1, n
    var mid int
    for lo < hi {
        mid = (lo + hi) / 2
        if !isBadVersion(mid) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}