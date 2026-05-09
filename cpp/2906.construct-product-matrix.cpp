#include <vector>
using std::vector;

class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        const int MOD = 12345;
        const int m = grid.size(), n = grid.front().size();
        vector<vector<int>> res(m, vector<int>(n, 1));
        long pre = 1, suf = 1;

        // prefix
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = pre;
                pre = pre * grid[i][j] % MOD;
            }
        }

        // suffix
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                res[i][j] = suf * res[i][j] % MOD;
                suf = suf * grid[i][j] % MOD;
            }
        }

        return res;
    }
};