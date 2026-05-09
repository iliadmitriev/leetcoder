
#include <queue>
#include <vector>

using namespace std;

class Solution {
private:
  typedef vector<vector<int>> Matrix;
  typedef pair<int, int> Point;

  Point findBoundary(const Matrix &land, Point start, Matrix &visited) {
    int rows = land.size();
    int cols = land[0].size();

    queue<Point> q;
    q.push(start);
    visited[start.first][start.second] = 1;
    Point dirs[2] = {{1, 0}, {0, 1}};
    Point p = start;

    while (!q.empty()) {
      p = q.front();
      q.pop();

      for (auto [dy, dx] : dirs) {
        int y = p.first + dy;
        int x = p.second + dx;

        if (0 <= y && y < rows && 0 <= x && x < cols && !visited[y][x] &&
            land[y][x]) {
          visited[y][x] = 1;
          q.push({y, x});
        }
      }
    }

    return p;
  }

public:
  vector<vector<int>> findFarmland(vector<vector<int>> &land) {
    int m = land.size(), n = land[0].size();
    Matrix visited(m, vector<int>(n, 0));

    Matrix res;

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (land[i][j] && !visited[i][j]) {
          Point p = findBoundary(land, {i, j}, visited);

          res.push_back({i, j, p.first, p.second});
        }
      }
    }

    return res;
  }
};