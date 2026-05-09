#include <vector>

using std::vector;

class Solution {
public:
  vector<int> lastVisitedIntegers(vector<int> &nums) {
    vector<int> ans, seen;
    int k = 0;

    for (int num : nums) {
      if (num > 0) {
        seen.push_back(num);
        k = 0;
      } else {
        if (seen.size() - k > 0) {
          ans.push_back(seen[seen.size() - ++k]);
        } else {
          ans.push_back(-1);
        }
      }
    }

    return ans;
  }
};