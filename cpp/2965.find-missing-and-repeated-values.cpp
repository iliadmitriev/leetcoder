#include <vector>

using std::vector;

class Solution {
public:
  vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid) {
    const int n = grid.size();
    vector<int> seen(n * n + 1, 0);

    int missing = 0;
    int repeated = 0;

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (seen[grid[i][j]]) {
          repeated = grid[i][j];
        }
        seen[grid[i][j]] += 1;
        missing ^= grid[i][j] ^ (i * n + j + 1);
      }
    }

    return {repeated, missing ^ repeated};
  }
};