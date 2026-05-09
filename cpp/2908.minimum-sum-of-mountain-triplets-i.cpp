#include <vector>
using std::vector;

class Solution {
public:
  int minimumSum(vector<int> &nums) {
    int n = nums.size();

    vector<int> left{nums.front()}, right{nums.back()};

    for (int i = 1; i < n; i++) {
      left.push_back(std::min(left.back(), nums[i]));
      right.push_back(std::min(right.back(), nums[n - i - 1]));
    }

    const int INF = int(1e9);
    int ans = INF;

    for (int i = 1; i < n - 1; i++) {
      if (nums[i] > left[i] && nums[i] > right[n - i - 1]) {
        ans = std::min(ans, left[i] + nums[i] + right[n - i - 1]);
      }
    }

    if (ans == INF) {
      return -1;
    }

    return ans;
  }
};