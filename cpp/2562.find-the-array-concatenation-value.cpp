#include <string>
#include <vector>

using std::vector;

class Solution {
private:
  long long concat(long long a, long long b) {
    auto t = b;

    while (b) {
      a *= 10;
      b /= 10;
    }

    return a + t;
  }

public:
  long long findTheArrayConcVal(vector<int> &nums) {
    long res = 0ll;

    int i = 0, j = nums.size() - 1;

    while (i < j) {
      res += concat(nums[i], nums[j]);
      i++;
      j--;
    }

    if (i == j) {
      res += nums[i];
    }

    return res;
  }
};