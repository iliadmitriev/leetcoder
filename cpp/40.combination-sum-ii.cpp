#include <algorithm>
#include <vector>

using std::sort;
using std::vector;

class Solution {
private:
  void backtrack(vector<int> &candidates, int target, int start,
                 vector<int> &path, vector<vector<int>> &res) {
    if (target < 0) {
      return;
    }
    if (target == 0) {
      res.push_back(path);
      return;
    }
    for (int i = start; i < candidates.size() && target >= candidates[i]; i++) {
      if (i > start && candidates[i] == candidates[i - 1]) {
        continue;
      }

      path.push_back(candidates[i]);
      backtrack(candidates, target - candidates[i], i + 1, path, res);
      path.pop_back();
    }
  }

public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {

    sort(candidates.begin(), candidates.end());

    vector<vector<int>> result;
    vector<int> path;

    backtrack(candidates, target, 0, path, result);

    return result;
  }
};