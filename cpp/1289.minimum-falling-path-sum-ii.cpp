#include <vector>

using namespace std;

class Solution {
private:
  pair<int, int> get_2_min_idx(const vector<int> &arr) {
    int i1 = -1, i2 = -1;
    int min1 = INT_MAX, min2 = INT_MAX;
    for (int i = 0; i < arr.size(); i++) {
      if (min1 > arr[i]) {
        min2 = min1;
        i2 = i1;
        min1 = arr[i];
        i1 = i;
      } else if (min2 > arr[i]) {
        min2 = arr[i];
        i2 = i;
      }
    }

    return {i1, i2};
  }

public:
  int minFallingPathSum(vector<vector<int>> &grid) {
    int height = grid.size(), width = grid[0].size();

    if (height == 1) {
      return grid[0][0];
    }

    vector<vector<int>> dp(height, vector<int>(width, 0));
    for (int j = 0; j < width; j++) {
      dp[0][j] = grid[0][j];
    }

    for (int i = 1; i < height; i++) {
      auto [j1, j2] = get_2_min_idx(dp[i - 1]);
      for (int j = 0; j < width; j++) {
        if (j != j1) {
          dp[i][j] = grid[i][j] + dp[i - 1][j1];
        } else {
          dp[i][j] = grid[i][j] + dp[i - 1][j2];
        }
      }
    }

    return *min_element(dp.back().begin(), dp.back().end());
  }
};