#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair;

class Solution {
public:
  int swimInWater(vector<vector<int>> &grid) {
    const int m = grid.size(), n = grid.front().size();
    const vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    typedef pair<int, int> Tile;
    typedef pair<int, Tile> Item;

    priority_queue<Item, vector<Item>, std::greater<Item>> pq;
    vector<vector<bool>> vis(m, vector<bool>(n, false));

    pq.push({grid[0][0], {0, 0}});
    vis[0][0] = true;

    while (!pq.empty()) {
      auto [height, tile] = pq.top();
      pq.pop();

      if (tile.first == m - 1 && tile.second == n - 1) {
        return height;
      }

      for (auto [dy, dx] : dirs) {
        int y = tile.first + dy, x = tile.second + dx;
        if (y < 0 || y >= m || x < 0 || x >= n || vis[y][x]) {
          continue;
        }

        pq.push({std::max(height, grid[y][x]), {y, x}});
        vis[y][x] = true;
      }
    }

    return -1;
  }
};