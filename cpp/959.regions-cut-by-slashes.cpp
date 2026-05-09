#include <queue>
#include <string>
#include <utility>
#include <vector>

using std::pair;
using std::queue;
using std::string;
using std::vector;

class Solution {
private:
  const vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

  void bfs(vector<vector<int>> &mat, int y, int x) {
    queue<pair<int, int>> q;
    int m = mat.size(), n = mat[0].size();
    q.push({y, x});
    mat[y][x] = 1;

    while (q.size()) {
      auto [y, x] = q.front();
      q.pop();

      for (auto [dy, dx] : dirs) {
        int ny = y + dy, nx = x + dx;
        if (0 <= ny && ny < m && 0 <= nx && nx < n && mat[ny][nx] == 0) {
          mat[ny][nx] = 1;
          q.push({ny, nx});
        }
      }
    }
  }

public:
  int regionsBySlashes(vector<string> &grid) {
    int islands = 0;

    int m = grid.size();
    int n = grid[0].size();

    vector<vector<int>> upscale(m * 3, vector<int>(n * 3, 0));

    // fill upscale matrix with 0 and 1
    for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
        if (grid[i][j] == '\\')
          for (int k = 0; k < 3; k++)
            upscale[i * 3 + k][j * 3 + k] = 1;
        else if (grid[i][j] == '/')
          for (int k = 0; k < 3; k++)
            upscale[i * 3 + k][j * 3 + 2 - k] = 1;

    for (int i = 0; i < m * 3; i++)
      for (int j = 0; j < n * 3; j++)
        if (upscale[i][j] == 0) {
          bfs(upscale, i, j);
          islands++;
        }

    return islands;
  }
};