#include <vector>
using std::vector;

class Solution {
private:
  int gcd(int a, int b) {
    while (a != b) {
      if (a > b) {
        a -= b;
      } else {
        b -= a;
      }
    }

    return a;
  }

public:
  int findGCD(vector<int> &nums) {
    return gcd(*max_element(nums.begin(), nums.end()),
               *min_element(nums.begin(), nums.end()));
  }
};