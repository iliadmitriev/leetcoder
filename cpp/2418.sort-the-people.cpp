#include <algorithm>
#include <string>
#include <utility>
#include <vector>

using std::pair;
using std::sort;
using std::string;
using std::vector;

class Solution {
public:
  vector<string> sortPeople(vector<string> &names, vector<int> &heights) {
    vector<pair<int, int>> tmp;
    for (int i = 0; i < heights.size(); ++i) {
      tmp.push_back({heights[i], i});
    }

    sort(tmp.begin(), tmp.end());

    vector<string> ret;
    for (int i = tmp.size() - 1; i >= 0; --i) {
      ret.push_back(names[tmp[i].second]);
    }
    return ret;
  }
};