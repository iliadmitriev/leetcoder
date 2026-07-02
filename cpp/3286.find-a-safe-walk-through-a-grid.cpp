class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        const int m = grid.size(), n = grid[0].size();
        const int sides[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        int finish_r = m - 1, finish_c = n - 1;

        health -= grid[0][0];

        priority_queue<pair<int, pair<int, int>>> pq;
        pq.push({health, {0, 0}});

        vector<vector<bool>> vis(m, vector<bool>(n, false));
        vis[0][0] = true;

        while (!pq.empty()) {
            auto [h, pos] = pq.top();
            pq.pop();

            auto [r, c] = pos;

            if (r == finish_r && c == finish_c) {
                return true;
            }

            for (auto& side : sides) {
                int nr = r + side[0], nc = c + side[1];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                int new_health = h - grid[nr][nc];

                if (new_health <= 0) {
                    continue;
                }

                if (vis[nr][nc]) {
                    continue;
                }

                vis[nr][nc] = true;
                pq.push({new_health, {nr, nc}});
            }
        }

        return false;
    }
};