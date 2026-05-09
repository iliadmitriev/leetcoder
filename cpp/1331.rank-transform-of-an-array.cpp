#include <algorithm>
#include <unordered_map>
#include <vector>

using std::unordered_map;
using std::vector;
class Solution {
public:
  vector<int> arrayRankTransform(vector<int> &arr) {
    vector<int> tmp = arr;
    std::sort(tmp.begin(), tmp.end());

    int j = 0;
    unordered_map<int, int> rankMap;

    for (int i = 0; i < tmp.size(); i++) {
      if (!rankMap.count(tmp[i])) {
        rankMap[tmp[i]] = ++j;
      }
    }

    std::transform(arr.begin(), arr.end(), arr.begin(),
                   [&](int x) { return rankMap[x]; });

    return arr;
  }
};