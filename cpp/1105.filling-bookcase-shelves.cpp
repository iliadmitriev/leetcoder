#include <vector>

using std::vector;

class Solution {
public:
  int minHeightShelves(vector<vector<int>> &books, int shelfWidth) {
    int n = books.size(), INF = int(1e9);
    vector<int> dp(n + 1, INF);
    dp[n] = 0;

    for (int i = n - 1; i >= 0; i--) {
      int w = 0, h = 0;
      for (int j = i; j < n; j++) {
        w += books[j][0];
        h = std::max(h, books[j][1]);
        if (w > shelfWidth)
          break;
        dp[i] = std::min(dp[i], dp[j + 1] + h);
      }
    }

    return dp[0];
  }
};