class SegmentTree {
private:
    static const int MAXK = 6;

    int k;
    int n;

    // indices [0, k-1] store the count of subarrays
    // index [k] stores the product.
    vector<array<int, MAXK>> tree;

    void makeLeaf(int o, int value) {
        tree[o].fill(0);
        int r = value % k;
        tree[o][r] = 1; // the count
        tree[o][k] = r; // the product
    }

    void mergePre(const array<int, MAXK>& left, const array<int, MAXK>& right,
                  array<int, MAXK>& result) {
        result.fill(0);

        int mulL = left[k];
        int mulR = right[k];
        result[k] = (mulL * mulR) % k;

        // case 1: entirely within the left interval
        for (int x = 0; x < k; x++) {
            result[x] = left[x];
        }

        // case 2: contain the entire left interval, followed by a prefix of
        // right interval
        for (int x = 0; x < k; x++) {
            result[(mulL * x) % k] += right[x];
        }
    }

    void build(const vector<int>& nums, int o, int l, int r) {
        if (l == r) {
            makeLeaf(o, nums[l]);
            return;
        }

        int m = (l + r) / 2;
        build(nums, o * 2, l, m);
        build(nums, o * 2 + 1, m + 1, r);

        // merge parent node from left and right children nodes
        mergePre(tree[o * 2], tree[o * 2 + 1], tree[o]);
    }

    void update(int o, int l, int r, int index, int value) {
        if (l == r) {
            makeLeaf(o, value);
            return;
        }
        int m = (l + r) / 2;
        if (index <= m) {
            update(o * 2, l, m, index, value);
        } else {
            update(o * 2 + 1, m + 1, r, index, value);
        }

        mergePre(tree[o * 2], tree[o * 2 + 1], tree[o]);
    }

    array<int, MAXK> query(int o, int l, int r, int L, int R) {
        if (L <= l && r <= R) {
            return tree[o];
        }

        int m = (l + r) / 2;
        if (R <= m) {
            return query(o * 2, l, m, L, R);
        }
        if (L > m) {
            return query(o * 2 + 1, m + 1, r, L, R);
        }

        auto left = query(o * 2, l, m, L, R);
        auto right = query(o * 2 + 1, m + 1, r, L, R);

        array<int, MAXK> res;
        mergePre(left, right, res);
        return res;
    }

public:
    SegmentTree(const vector<int>& nums, int k) : k(k), n(nums.size()) {
        int size = 2 << (int)ceil(log2(n));
        tree.resize(size);
        build(nums, 1, 0, n - 1);
    }

    void doUpdate(int index, int value) { update(1, 0, n - 1, index, value); }

    array<int, MAXK> doQuery(int L, int R) { return query(1, 0, n - 1, L, R); }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k,
                            vector<vector<int>>& queries) {
        int n = nums.size();
        SegmentTree seg(nums, k);
        vector<int> ans;

        for (auto& q : queries) {
            int index = q[0], value = q[1], start = q[2], x = q[3];

            seg.doUpdate(index, value);
            auto pre = seg.doQuery(start, n - 1);

            ans.push_back(pre[x]);
        }

        return ans;
    }
};