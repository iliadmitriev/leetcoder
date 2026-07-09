#include <vector>
using std::vector;

class UF {
private:
    int size;
    vector<int> par;

public:
    UF(int _size) : size(_size), par(_size) {
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
        int parx = find(x), pary = find(y);

        if (parx == pary) {
            return false;
        }

        par[pary] = parx;
        return true;
    }

    bool joined(int x, int y) {
        int parx = find(x), pary = find(y);

        return parx == pary;
    }
};

class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff,
                                      vector<vector<int>>& queries) {
        const int m = queries.size();
        vector<bool> res(m, false);
        UF uf(n);

        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] <= maxDiff) {
                uf.join(i - 1, i);
            }
        }

        for (int j = 0; j < m; j++) {
            const int u = queries[j][0];
            const int v = queries[j][1];

            res[j] = uf.joined(u, v);
        }

        return res;
    }
};