#include <queue>
#include <vector>

using namespace std;

class Solution {
private:
  void dfs(vector<vector<char>> &grid, int i, int j) {
    queue<pair<int, int>> q;
    q.push({i, j});
    grid[i][j] = '0';

    int m = grid.size(), n = grid[0].size();
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    while (!q.empty()) {
      auto [i, j] = q.front();
      q.pop();
      for (auto [di, dj] : dirs) {
        int ni = i + di, nj = j + dj;
        if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == '1') {
          q.push({ni, nj});
          grid[ni][nj] = '0';
        }
      }
    }
  }

public:
  int numIslands(vector<vector<char>> &grid) {
    int m = grid.size(), n = grid[0].size();
    int islands = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '1') {
          islands++;
          dfs(grid, i, j);
        }
      }
    }

    return islands;
  }
};