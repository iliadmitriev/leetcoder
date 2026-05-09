#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class Solution {
public:
  int countCoveredBuildings(int n, vector<vector<int>> &buildings) {
    int covered = 0;
    unordered_map<int, vector<int>> hor;
    unordered_map<int, vector<int>> ver;

    for (auto &b : buildings) {
      int x = b[0], y = b[1];

      hor[x].push_back(y);
      ver[y].push_back(x);
    }

    for (auto &[_, ys] : hor) {
      std::sort(ys.begin(), ys.end());
    }

    for (auto &[_, xs] : ver) {
      std::sort(xs.begin(), xs.end());
    }

    for (auto &[x, ys] : hor) {

      for (int i = 1; i < ys.size() - 1; i++) {

        int y = ys[i];

        if (ver[y].front() < x && x < ver[y].back()) {
          covered++;
        }
      }
    }

    return covered;
  }
};