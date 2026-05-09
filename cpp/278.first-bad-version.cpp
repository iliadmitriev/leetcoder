// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long lo = 1;
        long hi = n;
        long mid;

        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (!isBadVersion(mid)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
};