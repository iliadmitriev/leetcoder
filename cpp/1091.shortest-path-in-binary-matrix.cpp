typedef pair<int, int> Point; // (row, col) or (y, x)

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size(); // rows
        int n = grid.size(); // cols

        // if finish or start is an obstacle then no need to run algo
        if (grid[0][0] == 1 || grid[m - 1][n - 1] == 1) {
            return -1;
        }

        // heuristic function for distance evaluation from finish point
        auto _f = [m, n](const Point& p) -> int {
            return max(m - p.first, n - p.second);
        };
        // less function between two point
        auto less_fn = [&_f](const Point& p1, const Point& p2) -> bool {
            return _f(p1) < _f(p2);
        };

        // priority queue
        priority_queue<Point, vector<Point>, decltype(less_fn)> pq(less_fn);
        pq.push(make_pair(0, 0));

        // map for cells distances (init as Infinity) 
        vector<vector<int>> distances(m, vector<int>(n, int(1e9)));
        distances[0][0] = 1;

        // 8 steps
        pair<int, int> steps[8] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

        while (!pq.empty()) {
            auto [r, c] = pq.top(); pq.pop();

            if (r == m - 1 && c == n - 1) {
                return distances[r][c];
            }

            for (auto [dy, dx] : steps) {
                int y = r + dy;
                int x = c + dx;
                if (y < 0 || y >= m || x < 0 || x >= n || grid[y][x] == 1) {
                    continue;
                }

                if (distances[r][c] + 1 < distances[y][x]) {
                    pq.push(make_pair(y, x));
                    distances[y][x] = distances[r][c] + 1;
                }
            }
        }

        return -1;
    }
};