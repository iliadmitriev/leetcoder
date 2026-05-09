#include <functional>
#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::greater, std::max, std::pair;

class Solution {
public:
  typedef pair<int, int> Point;
  typedef pair<int, Point> Item;
  typedef priority_queue<Item, vector<Item>, greater<Item>> MinHeap;

  int trapRainWater(vector<vector<int>> &heightMap) {
    const int NROWS = heightMap.size(), NCOLS = heightMap.back().size();
    const auto DIRS = vector<Point>{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    vector<vector<bool>> visited(NROWS, vector<bool>(NCOLS, false));
    MinHeap heap;
    int maxHeight = 0, res = 0;

    for (int i = 0; i < NROWS; ++i) {
      heap.push({heightMap[i][0], {i, 0}});
      heap.push({heightMap[i][NCOLS - 1], {i, NCOLS - 1}});
      visited[i][0] = visited[i][NCOLS - 1] = true;
    }

    for (int j = 0; j < NCOLS; ++j) {
      heap.push({heightMap[0][j], {0, j}});
      heap.push({heightMap[NROWS - 1][j], {NROWS - 1, j}});
      visited[0][j] = visited[NROWS - 1][j] = true;
    }

    while (!heap.empty()) {
      auto [height, point] = heap.top();
      heap.pop();

      maxHeight = max(maxHeight, height);
      res += maxHeight - height;

      for (auto [dr, dc] : DIRS) {
        int r = point.first + dr, c = point.second + dc;
        if (r < 0 || r >= NROWS || c < 0 || c >= NCOLS || visited[r][c]) {
          continue;
        }

        visited[r][c] = true;
        heap.push({heightMap[r][c], {r, c}});
      }
    }

    return res;
  }
};