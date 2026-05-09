class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        // accumulative matrix
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j]) {
                    matrix[i][j] += matrix[i - 1][j];
                }
            }
        }

        int res = 0;
        for (auto& row: matrix) {
            std::sort(row.begin(), row.end(), std::greater<>());
            for (int j = 0; j < n && row[j] > 0; j++) {
                res = max(res, row[j] * (j + 1));
            }
        }

        return res;
    }
};