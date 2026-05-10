#include <algorithm>
#include <unordered_set>
#include <vector>

using std::vector, std::unordered_set;

int bisectLeft(const vector<long>& arr, long target) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
        mid = (lo + hi) / 2;

        if (arr[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return lo;
}

int bisectRight(const vector<long>& arr, long target) {
    int lo = 0, hi = arr.size();
    int mid;

    while (lo < hi) {
        mid = (lo + hi) / 2;

        if (arr[mid] <= target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    return lo;
}

// Segment Tree (Segmented Tree): query, update
// max segment tree
class SegmentTree {
private:
    int size;
    vector<int> tree;

    // update tree with value (val), starting from node
    // in range [start, end]
    void _update(int idx, int val, int node, int start, int end) {
        if (start == end) {
            tree[node] = std::max(tree[node], val);
            return;
        }

        int mid = (start + end) / 2;

        if (idx <= mid) {
            _update(idx, val, 2 * node, start, mid);
        } else {
            _update(idx, val, 2 * node + 1, mid + 1, end);
        }

        // update parent node
        tree[node] = std::max(tree[2 * node], tree[2 * node + 1]);
    }

    // query (return max)
    int _query(int l, int r, int node, int start, int end) {
        if (r < start || end < l) {
            return -1;
        }

        if (l <= start && end <= r) {
            return tree[node];
        }

        int mid = (start + end) / 2;
        int left = _query(l, r, 2 * node, start, mid);
        int right = _query(l, r, 2 * node + 1, mid + 1, end);

        return std::max(left, right);
    }

public:
    SegmentTree(int _size) : size(_size), tree(4 * _size, -1) {}

    void update(int idx, int val) { _update(idx, val, 1, 0, size - 1); }
    int query(int l, int r) { return _query(l, r, 1, 0, size - 1); }
};

class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {

        const int n = nums.size();

        // sorted unique nums `sorted`
        unordered_set<int> tmp(nums.begin(), nums.end());
        vector<long> sorted(tmp.begin(), tmp.end());
        std::sort(sorted.begin(), sorted.end());

        vector<int> dp(n, -1); // number of max jumps starting from i to n - 1
        dp[n - 1] = 0;         // base case 0 number of jumps to n - 1
        // -1 means no connection

        SegmentTree st = SegmentTree(sorted.size());
        int idx = bisectLeft(sorted, nums[n - 1]); // sorted index of last element
        st.update(idx, 0); // update it with 0

        for (int i = n - 2; i >= 0; i--) {
          long leftVal = long(nums[i]) - target;
          long rightVal = long(nums[i]) + target;

          int l = bisectLeft(sorted, leftVal);
          int r = bisectRight(sorted, rightVal) - 1;

          if (l <= r) {
            int best = st.query(l, r);

            if (best != -1) {
              dp[i] = best + 1;
            }
          }

          if (dp[i] != -1) {
            idx = bisectLeft(sorted, nums[i]);
            st.update(idx, dp[i]);
          }
        }

        return dp[0];
    }
};