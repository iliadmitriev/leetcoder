class UnionFind {
    vector<int> par, rank, arr;

public:

    UnionFind(int n, vector<int>& data) : par(n), rank(n, 1), arr(data) {
        std::iota(par.begin(), par.end(), 0);
    }

    int find(int x) {
        while (x != par[x]) {
            par[x] = par[par[x]];
            x = par[x];
        }
        return x;
    }

    bool join(int x, int y) {
        int px = find(x), py = find(y);

        if (px == py) {
          return false;
        }

        if (rank[px] < rank[py]) {
          std::swap(px, py);
        }

        par[py] = px;
        rank[px] += rank[py];
        arr[px] = max(arr[px], arr[py]);

        return true;
    }

    int getValue(int x) { return arr[find(x)]; }
};

class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        const int n = nums.size();

        vector<int> pre(n), suf(n); // preffix and suffix max

        pre[0] = nums[0];
        for(int i = 1; i < n; i++) {
            pre[i] = max(pre[i - 1], nums[i]);
        }

        suf[n - 1] = nums[n - 1];
        for(int i = n - 2; i >= 0; i--) {
            suf[i] = min(suf[i + 1], nums[i]);
        }

        // UnionFind uf(n, nums);

        // for (int i = 0; i < n - 1; i++) {
        //     if (pre[i] > suf[i + 1]) {
        //         uf.join(i, i + 1);
        //     }
        // }

        vector<int> res(n);
        res[n - 1] = pre[n - 1];

        // for (int i = 0; i < n; i++) {
        //     res[i] = uf.getValue(i);
        // }

        for (int i = n - 2; i >= 0; i--) {
          if (pre[i] > suf[i + 1]) { // contiguous segment
            res[i] = res[i + 1];
          } else { // segment breaks here
            res[i] = pre[i];
          }
        }

        return res;
    }
};