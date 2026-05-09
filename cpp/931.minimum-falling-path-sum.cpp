class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix.size(); int n = matrix.size() ? matrix[0].size() : 0;

        vector<vector<int>> cache(2, vector<int>(n, 0));

        int down, left, right;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                down = matrix[i][j] + cache[(i + 1) % 2][j];
                left = down; right = down; 
                
                if (j > 0) {
                    left = matrix[i][j] + cache[(i + 1) % 2][j - 1];
                }

                if (j < n - 1) {
                    right = matrix[i][j] + cache[(i + 1) % 2][j + 1];
                }

                cache[i % 2][j] = min(down, min(left, right));
            }
        }

        int res = INT_MAX;

        for (int j = 0; j < n; j++) {
            res = min(res, cache[(m + 1) % 2][j]);
        }

        return res;
    }
};