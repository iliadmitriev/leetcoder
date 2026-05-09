#include <limits>
#include <vector>
using std::vector;

class Solution {
public:
  int thirdMax(vector<int> &nums) {
    if (nums.size() < 3) {
      return *std::max_element(nums.begin(), nums.end());
    }

    const long NEG_INF = std::numeric_limits<long>::min();
    long S = NEG_INF, M = NEG_INF, L = NEG_INF;

    for (int num : nums) {
      if (L < num) {
        S = M;
        M = L;
        L = num;
      } else if (M < num && L != num) {
        S = M;
        M = num;
      } else if (S < num && M != num && L != num) {
        S = num;
      }
    }

    if (S == NEG_INF) {
      return L;
    }

    return S;
  }
};