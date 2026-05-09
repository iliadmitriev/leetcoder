#include <map>
#include <vector>

using std::map;
using std::vector;

class Solution {
public:
  vector<vector<int>> mergeSimilarItems(vector<vector<int>> &items1,
                                        vector<vector<int>> &items2) {
    map<int, int> merge;

    for (int i = 0; i < items1.size(); ++i) {
      merge[items1[i][0]] += items1[i][1];
    }

    for (int i = 0; i < items2.size(); ++i) {
      merge[items2[i][0]] += items2[i][1];
    }

    vector<vector<int>> ans;
    ans.reserve(merge.size());

    for (auto [k, v] : merge) {
      ans.push_back({k, v});
    }

    return ans;
  }
};