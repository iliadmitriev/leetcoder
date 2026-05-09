#include <functional>
#include <queue>
#include <utility>
#include <vector>

using std::vector, std::pair, std::priority_queue, std::greater;

class Solution {
public:
  typedef vector<vector<int>> Matrix;
  typedef pair<int, int> Position;
  typedef pair<int, Position> State;

  const State DIRS[4] = {{1, {0, 1}}, {2, {0, -1}}, {3, {1, 0}}, {4, {-1, 0}}};

  void makeSteps(Position &pos, int cost, Matrix &grid,
                 std::function<void(Position &, int)> f) {
    const int m = grid.size(), n = grid[0].size();
    auto [y, x] = pos;

    for (auto [dir, step] : DIRS) {
      auto [dy, dx] = step;
      int newY = y + dy, newX = x + dx;

      if (newY < 0 || newY >= m || newX < 0 || newX >= n) {
        continue;
      }

      Position newPos = {newY, newX};
      int addedCost = dir == grid[y][x] ? 0 : 1;

      f(newPos, cost + addedCost);
    }
  }

  int minCost(vector<vector<int>> &grid) {
    const int m = grid.size(), n = grid[0].size();
    const Position start = {0, 0}, end = {m - 1, n - 1};
    const int INF = int(1e9);

    priority_queue<State, vector<State>, greater<State>> pq;
    pq.push({0, start});

    Matrix dist(m, vector<int>(n, INF));
    dist[start.first][start.second] = 0;

    while (!pq.empty()) {
      auto [cost, pos] = pq.top();
      pq.pop();

      if (pos == end) {
        return cost;
      }

      makeSteps(
          pos, cost, grid,
          [&dist, &pq](Position &newPos, int newCost) {
            auto [newY, newX] = newPos;

            if (dist[newY][newX] > newCost) {
              dist[newY][newX] = newCost;
              pq.push({newCost, newPos});
            }
          });
    }

    return -1;
  }
};