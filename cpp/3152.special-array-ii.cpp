#include <vector>
using std::vector;

class Solution {
public:
  vector<bool> isArraySpecial(vector<int> &nums, vector<vector<int>> &queries) {
    const int n = nums.size(), m = queries.size();

    vector<int> prefix;
    int prev = (nums.front() + 1) % 2;

    for (int i = 0; i < n; i++) {
      if (prev + nums[i] % 2 != 1) {
        prefix.push_back(i);
      }
      prev = nums[i] % 2;
    }

    vector<bool> result(m, true);

    for (int j = 0; j < m; j++) {
      if (queries[j][0] == queries[j][1]) {
        continue;
      }

      int left = searchRight(prefix, queries[j][0]);
      int right = searchRight(prefix, queries[j][1]);
      result[j] = left == right;
    }

    return result;
  }

private:
  int searchRight(const vector<int> &nums, int target) {
    int lo = 0, hi = nums.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;
      if (target < nums[mid]) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }
};