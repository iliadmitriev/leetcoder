#include <algorithm>
#include <vector>
using std::max;
using std::min;
using std::vector;

class Solution {
public:
  int maxDistance(vector<vector<int>> &arrays) {
    int minItem = arrays[0][0];
    int maxItem = arrays[0][arrays[0].size() - 1];

    int res = 0;

    for (int i = 1; i < arrays.size(); i++) {
      res = max(res, max(arrays[i][arrays[i].size() - 1] - minItem,
                         maxItem - arrays[i][0]));

      minItem = min(minItem, arrays[i][0]);
      maxItem = max(maxItem, arrays[i][arrays[i].size() - 1]);
    }

    return res;
  }
};