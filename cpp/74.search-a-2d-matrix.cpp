class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0, col = matrix[0].size() - 1;

        while (row < matrix.size() && col >= 0) {
            int curr = matrix[row][col];
            if (target < curr) {
                col--;
            } else if (target > curr) {
                row++;
            } else {
                return true;
            };

        };

        return false;
    }
};