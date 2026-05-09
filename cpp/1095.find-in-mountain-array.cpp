/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
private:
    unordered_map<int, int> _cache;
    MountainArray* _m;

    int _get(int key) {
        if (_cache.find(key) != _cache.end()) {
            return _cache[key];
        }
        return _cache[key] = _m->get(key);
    }

    int _bsearch(int lo, int hi, std::function<bool(int)> fn) {
        int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (fn(mid)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        // set cache
        _cache.clear();
        _m = &mountainArr;
        int len = _m->length();

        // find peak
        int peak = _bsearch(1, len - 2, [&](int mid) -> bool {
            return _get(mid) < _get(mid + 1);
        });

        // find min in left increasing part
        int left = _bsearch(0, peak, [&](int mid) -> bool {
            return _get(mid) < target;
        });
        if (_get(left) == target) {
            return left;
        }

        // find min in right decreasing part
        int right = _bsearch(peak + 1, len - 1, [&](int mid) -> bool {
            return _get(mid) > target;
        });
        if (_get(right) == target) {
            return right;
        }
        
        // return -1 otherwise
        return -1;
    }
};