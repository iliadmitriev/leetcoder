#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

long long inline posKey(int x, int y) {
  return ((long long)x << 32) | (y & 0xFFFFFFFFLL);
}

class Solution {
public:
  int robotSim(vector<int> &commands, vector<vector<int>> &obstacles) {
    int x = 0, y = 0;
    int dx = 0, dy = 1;

    int farest = 0;

    unordered_set<long long> obs;
    for (auto &o : obstacles) {
      obs.insert(posKey(o[0], o[1]));
    }

    for (int cmd : commands) {
      if (cmd == -1) {
        std::swap(dx, dy);
        dy = -dy;
      } else if (cmd == -2) {
        std::swap(dx, dy);
        dx = -dx;
      } else {
        for (; cmd; cmd--) {
          int nx = x + dx;
          int ny = y + dy;
          if (obs.count(posKey(nx, ny))) {
            break;
          }

          x = nx;
          y = ny;
        }
      }

      farest = std::max(farest, x * x + y * y);
    }

    return farest;
  }
};