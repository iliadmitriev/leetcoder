typedef pair<int, int> Point;

class Solution {
private:
    // find any land for a starting point
    Point findStart(vector<vector<int>>& grid) {
        auto m = grid.size();
        auto n = grid[0].size();
        for (auto i = 0; i < m; i++) {
            for (auto j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    return make_pair(i, j);
                }
            }
        }
        return make_pair(0, 0);
    }

    // find all connected cells (whole island)
    // mark them as visited and put them into `vis`
    vector<Point> dfs(Point start, vector<vector<bool>>& vis, vector<vector<int>>& grid) {
        auto m = grid.size();
        auto n = grid[0].size();
        int phase[5] = {-1, 0, 1, 0, -1};
        vector<Point> res;

        stack<Point> st;
        st.push(start);
        vis[start.first][start.second] = true;

        while (!st.empty()) {
            auto node = st.top(); st.pop();
            res.push_back(node);

            for (int i = 0; i < 4; i++) {
                auto r = node.first + phase[i];
                auto c = node.second + phase[i + 1];

                if (0 <= r && r < m && 0 <= c && c < n && !vis[r][c] && grid[r][c]) {
                    vis[r][c] = true;
                    st.push(make_pair(r, c));
                }
            }
        }
        return res;
    }

    // find shortest path from visited island `island` to second island
    int bfs(vector<Point>& island, vector<vector<bool>>& vis, vector<vector<int>>& grid) {
        auto m = grid.size();
        auto n = grid[0].size();
        int phase[5] = {-1, 0, 1, 0, -1};
        
        // point coordinates (row, col) and it's distance from island
        queue<pair<Point, int>> que;
        // add all island coordinates with 0 distance
        for (const auto& p : island) {
            que.push(make_pair(p, 0));
        }

        while (!que.empty()) {
            auto [point, distance] = que.front(); que.pop();


            for (int i = 0; i < 4; i++) {
                auto r = point.first + phase[i];
                auto c = point.second + phase[i + 1];
                if (0 <= r && r < m && 0 <= c && c < n && !vis[r][c]) {
                    if (grid[r][c] == 1) {
                        return distance;
                    } else {
                        vis[r][c] = true;
                        que.push(make_pair(make_pair(r, c), distance + 1));
                    }
                }
            }
        }

        return -1;
    }

public:
    int shortestBridge(vector<vector<int>>& grid) {
        auto m = grid.size();
        auto n = grid[0].size();
        vector<vector<bool>> vis(m, vector<bool>(n, false));

        auto start = findStart(grid);
        auto island = dfs(start, vis, grid);

        return bfs(island, vis, grid);
    }
};