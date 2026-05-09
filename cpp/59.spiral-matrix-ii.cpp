class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // start generator
        int gen = 0;
        // result vector;
        vector<vector<int>> res(n, vector<int>(n, 0));
        // number of loops
        int loops = n / 2;

        for (int l = 0; l < loops; l++) {
            // fill top row [left + loop; right - loop - 1]
            for (int c = l; c < n - l - 1; c++) {
                res[l][c] = ++gen;
            }
            // fill right column [top + loop; bottom - loop - 1]
            for (int r = l; r < n - l - 1; r++) {
                res[r][n - l - 1] = ++gen;
            }
            // fill bottom row
            for (int c = n - l - 1; c > l; c--) {
                res[n - l - 1][c] = ++gen;
            }
            // fill left column
            for (int r = n - l - 1; r > l; r--) {
                res[r][l] = ++gen;
            }
        }

        if (n % 2) {
            res[n / 2][n / 2] = ++gen;
        }

        return res;
    }
};