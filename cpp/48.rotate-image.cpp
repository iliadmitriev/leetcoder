#include <vector>
using std::vector;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        for (int i = 0; i < n / 2 + n % 2; i++) {
            for (int j = 0; j < n / 2; j++) {
                // swap values counterclockwise
                // save bottom left corner to temp
                int tmp = matrix[n - 1 - j][i];
                // move bottom right to bottom left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                // move top right to bottom right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                // move top left to top right
                matrix[j][n - 1 - i] = matrix[i][j];
                // set top left from saved bottom left
                matrix[i][j] = tmp;
            }
        }
    }
};