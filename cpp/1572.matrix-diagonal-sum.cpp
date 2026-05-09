class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int i = 0, n = mat.size();
        int total = 0;
        for (const auto& row: mat) {
            total += row[i] + row[n - ++i];
        }
        if (n % 2) {
            total -= mat[n / 2][n / 2];
        }
        return total;
    }
};