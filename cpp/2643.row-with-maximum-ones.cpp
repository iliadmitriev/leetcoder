#include <numeric>
#include <vector>
using std::vector;

class Solution {
public:
  vector<int> rowAndMaximumOnes(vector<vector<int>> &mat) {
    vector<int> res = {0, 0};
    int curRowCount = 0;

    for (int i = 0; i < mat.size(); i++) {
      curRowCount = std::accumulate(mat[i].begin(), mat[i].end(), 0);

      if (curRowCount > res[1]) {
        res[0] = i;
        res[1] = curRowCount;
      }
    }

    return res;
  }
};