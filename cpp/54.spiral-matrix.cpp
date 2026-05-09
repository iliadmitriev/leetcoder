class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top = 0, left = 0,
            bottom = matrix.size() - 1,
            right = matrix[0].size() - 1;

        vector<int> res;
        res.reserve(matrix.size() * matrix[0].size());

        while (top <= bottom && left <= right) {
            // top row
            for (int c = left; c <= right; c++) {
                res.push_back(matrix[top][c]);
            }
            top++;

            // right column
            for (int r = top; r <= bottom; r++) {
                res.push_back(matrix[r][right]);
            }
            right--;

            if (top <= bottom) {
                // bottom row (reversed)
                for (int c = right; c >= left; c--) {
                    res.push_back(matrix[bottom][c]);
                }
                bottom--;
            }

            if (left <= right) {
                // left column (revered)
                for (int r = bottom; r >= top; r--) {
                    res.push_back(matrix[r][left]);
                }
                left++;
            }
        }

        return res;
    }
};