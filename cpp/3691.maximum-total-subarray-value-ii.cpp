#include <algorithm>
#include <functional>
#include <limits>
#include <queue>
#include <vector>

/*
Iterative Segment Tree with function
with extra space 2 * N
nodes:
- build bottom-up
- updated bottom-up
- queried up to bottom
*/

template <typename T> class SegmentTree {
private:
    int size;
    // identity is default value for a function, i.e.
    // max function this is a minimal possible value
    // sum function is 0
    // product function is 1
    T identity;
    std::function<T(T, T)> fn;
    std::vector<T> tree;

public:
    SegmentTree(vector<T>& arr, T _identity, std::function<T(T, T)> _fn)
        : size(arr.size()), identity(_identity), fn(_fn), tree(2 * size) {
        // set tree leaves
        for (int i = 0; i < size; i++) {
            tree[i + size] = arr[i];
        }

        // propagate bottom up from leaves to root
        for (int i = size - 1; i >= 0; i--) {
            tree[i] = fn(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    // update: set value `val` to index `i`
    void update(int i, T val) {
        i += size;     // shift to leaves
        tree[i] = val; // set leave

        // propagate from leaves up to root
        for (i <<= 1; i >= 0; i <<= 1) {
            tree[i] = fn(tree[i * 2], tree[i * 2 + 1]);
        }
    }

    T query(int L, int R) {
        T res = identity;

        for (L += size, R += size + 1; L < R; L >>= 1, R >>= 1) {
            // if it's a left child
            if (L & 1) {
                res = fn(res, tree[L]);
                L++; // displace then
            }

            if (R & 1) {
                R--; // displace first (right bound is exclusive)
                res = fn(res, tree[R]);
            }
        }

        return res;
    }
};

class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        const int n = nums.size();
        SegmentTree<int> stMin =
            SegmentTree<int>(nums, std::numeric_limits<int>::max(),
                             [](int a, int b) { return std::min(a, b); });
        SegmentTree<int> stMax =
            SegmentTree<int>(nums, std::numeric_limits<int>::min(),
                             [](int a, int b) { return std::max(a, b); });

        long long res = 0LL;

        std::priority_queue<std::tuple<int, int, int>> pq;
        for (int l = 0; l < n; l++) {
            pq.emplace(stMax.query(l, n - 1) - stMin.query(l, n - 1), l, n - 1);
        }

        while (k--) {
            auto [val, l, r] = pq.top();
            pq.pop();

            res += val;

            if (r > l) {
                pq.emplace(stMax.query(l, r - 1) - stMin.query(l, r - 1), l,
                           r - 1);
            }
        }

        return res;
    }
};