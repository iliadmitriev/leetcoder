#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

using std::vector, std::string, std::unordered_map;

class Solution {
public:
  int maxEqualRowsAfterFlips(vector<vector<int>> &matrix) {
    unordered_map<string, int> count;

    for (const vector<int> &row : matrix) {
      int n = row.size();
      string rowInv(n, 0);
      for (int i = 0; i < n; i++) {
        rowInv[i] = '0' + (1 - row[i] != row[0]);
      }

      count[rowInv]++;
    }

    return std::accumulate(
        count.begin(), count.end(), 0,
        [](int acc, const auto &kv) { return std::max(acc, kv.second); });
  }
};