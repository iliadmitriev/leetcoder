class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        auto m = obstacleGrid.size(), n = obstacleGrid[0].size();

        if (obstacleGrid[0][0] || obstacleGrid[m - 1][n - 1])
            return 0;

        int grid[m][n];
        memset(grid, 0, sizeof(grid));
        
        // mark start with a single way to get there
        grid[0][0] = 1;

        // there is two ways to get in any cell:
        //  * moving down from upper cell
        //  * moving right from left cell
        // all the ways to get to any cell is the sum of these both
        // (if there is no obstable)
        for (auto i = 0; i < m; i++)
            for (auto j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1)
                    continue;
                if (i > 0)
                    grid[i][j] += grid[i - 1][j];
                if (j > 0)
                    grid[i][j] += grid[i][j - 1];

            };

        return grid[m - 1][n - 1];
    }
};