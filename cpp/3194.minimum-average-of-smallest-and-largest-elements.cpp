#include <algorithm>
#include <limits>
#include <vector>

using std::vector;

class Solution {
private:
  inline double min(double a, double b) { return a < b ? a : b; }

public:
  double minimumAverage(vector<int> &nums) {
    double minAvg = std::numeric_limits<float>::infinity();
    int n = nums.size();
    std::sort(nums.begin(), nums.end());

    for (int i = 0; i < n / 2; i++) {
      minAvg = min(minAvg, double(nums[i] + nums[n - 1 - i]) / 2.0f);
    }

    return minAvg;
  }
};