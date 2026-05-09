#include <vector>
using std::vector;

class Solution {
public:
  vector<vector<int>> rangeAddQueries(int n, vector<vector<int>> &queries) {
    vector<vector<int>> prefix(n + 1, vector<int>(n + 1, 0));
    vector<vector<int>> res(n, vector<int>(n, 0));

    for (auto &q : queries) {
      prefix[q[0]][q[1]]++;
      prefix[q[0]][q[3] + 1]--;
      prefix[q[2] + 1][q[1]]--;
      prefix[q[2] + 1][q[3] + 1]++;
    }

    for (int i = 0; i < n; i++) {
      int row = 0;
      for (int j = 0; j < n; j++) {
        row += prefix[i][j];
        res[i][j] = row;

        if (i == 0) {
          continue;
        }

        res[i][j] += res[i - 1][j];
      }
    }

    return res;
  }
};