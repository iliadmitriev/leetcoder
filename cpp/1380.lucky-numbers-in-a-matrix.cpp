
#include <unordered_set>
#include <vector>

using std::unordered_set;
using std::vector;

class Solution {
public:
  vector<int> luckyNumbers(vector<vector<int>> &matrix) {
    vector<int> lucky;

    int m = matrix.size(), n = matrix[0].size();
    unordered_set<int> minRows;

    for (int i = 0; i < m; ++i) {
      minRows.insert(*min_element(matrix[i].begin(), matrix[i].end()));
    }

    for (int i = 0; i < n; ++i) {
      int maxCol = matrix[0][i];
      for (int j = 1; j < m; ++j) {
        if (matrix[j][i] > maxCol) {
          maxCol = matrix[j][i];
        }
      }
      if (minRows.count(maxCol)) {
        lucky.push_back(maxCol);
      }
    }

    return lucky;
  }
};