#include <numeric>
#include <vector>

#include <cstdlib>

using std::vector;

class Solution {
private:
  int digitSum(int n) {
    int s = 0;
    while (n) {
      s += n % 10;
      n /= 10;
    }

    return s;
  }

public:
  int differenceOfSum(vector<int> &nums) {
    int total = std::accumulate(nums.begin(), nums.end(), 0);
    int totalDigitSum =
        accumulate(nums.begin(), nums.end(), 0,
                   [&](int a, int b) -> int { return a + digitSum(b); });
    return abs(total - totalDigitSum);
  }
};