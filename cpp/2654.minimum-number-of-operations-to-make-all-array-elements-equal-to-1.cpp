#include <vector>
using std::vector;

class Solution {
private:
  int gcd(int a, int b) {
    while (b) {

      a %= b;
      std::swap(a, b);
    }

    return a;
  }

public:
  int minOperations(vector<int> &nums) {

    int n = nums.size();
    int cnt1 = std::count(nums.begin(), nums.end(), 1);

    if (cnt1) {
      return n - cnt1;
    }

    for (int d = 2; d <= n; d++) {
      for (int i = 0; i < n - d + 1; i++) {
        int g = gcd(nums[i], nums[i + 1]);
        nums[i] = g;

        if (g == 1) {
          return d + n - 2;
        }
      }
    }

    return -1;
  }
};