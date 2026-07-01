#include <numeric>
#include <queue>
#include <utility>
#include <vector>

using std::vector, std::pair;

class Solution {
private:
    typedef tuple<int, int, int> P;

public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size();
        int MAX_INT = numeric_limits<int>::max();

        vector<vector<int>> thieves(ROWS, vector<int>(COLS, MAX_INT));
        queue<pair<int, int>> q;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) {
                    thieves[r][c] = 0;
                    q.push({r, c});
                }
            }
        }

        const vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (q.size()) {
            auto [r, c] = q.front();
            q.pop();

            for (auto [dr, dc] : dirs) {
                int nr = r + dr, nc = c + dc;

                if (0 > nr || nr >= ROWS || 0 > nc || nc >= COLS) {
                    continue;
                }
                if (thieves[nr][nc] == MAX_INT ||
                    thieves[nr][nc] > thieves[r][c] + 1) {
                    thieves[nr][nc] = thieves[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }

        priority_queue<P, vector<P>, less<P>> pq;
        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
        visited[0][0] = true;
        pq.push({thieves[0][0], 0, 0});

        while (pq.size()) {
            auto [d, r, c] = pq.top();
            pq.pop();

            if (r == ROWS - 1 && c == COLS - 1) {
                return d;
            }

            for (auto [dr, dc] : dirs) {
                int nr = r + dr, nc = c + dc;

                if (0 > nr || nr >= ROWS || 0 > nc || nc >= COLS) {
                    continue;
                }

                if (visited[nr][nc]) {
                    continue;
                }

                int nd = min(d, thieves[nr][nc]);
                pq.push({nd, nr, nc});
                visited[nr][nc] = true;
            }
        }

        return -1;
    }
};