class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        const int m = grid.size(), n = grid.front().size();

        long all = 0, left = 0, top = 0;
        long target = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                all += grid[i][j];
            }
        }

        // if it's not odd, then it's impossible to split it in two equal parts
        if (all % 2) {
            return false;
        }

        target = all / 2; // exact value to collect

        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) {
                top += grid[i][j];
            }

            if (top == target) {
                return true;
            }

            if (top > target) { // skip if over the target
              break;
            }
        }

        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) {
                left += grid[i][j];
            }

            if (left == target) {
                return true;
            }

            if (left > target) { // skip if over the target
              break;
            }
        }

        return false;
    }
};