class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        const int m = grid.size();
        const int n = grid.front().size();
        const int path_len = m + n - 1;

        if (path_len % 2 == 1 || grid[0][0] == ')' ||
            grid[m - 1][n - 1] == '(') {
            return false;
        }

        // dp memo
        std::vector<std::vector<std::vector<int>>> memo(
            m, std::vector<std::vector<int>>(
                   n, std::vector<int>(path_len + 1, -1)));

        auto dfs = [&](auto& self, int i, int j, int cnt) -> bool {
            if (i == m || j == n)
                return false;

            cnt += (grid[i][j] == '(') ? 1 : -1;

            if (cnt < 0)
                return false;
            if (cnt > path_len / 2)
                return false;

            if (i == m - 1 && j == n - 1)
                return cnt == 0;

            if (memo[i][j][cnt] != -1)
                return memo[i][j][cnt];

            return memo[i][j][cnt] =
                       self(self, i + 1, j, cnt) || self(self, i, j + 1, cnt);
        };

        return dfs(dfs, 0, 0, 0);
    }
};