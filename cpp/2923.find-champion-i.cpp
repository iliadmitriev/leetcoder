#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  int findChampion(vector<vector<int>> &grid) {
    const int n = grid.size();

    for (int i = 0; i < n; ++i) {
      if (std::accumulate(grid[i].begin(), grid[i].end(), 0) == n - 1) {
        return i;
      }
    }

    return -1;
  }
};