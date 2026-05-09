#include <vector>

using std::vector;

class Solution {
public:
  int specialTriplets(vector<int> &nums) {

    typedef int ll;

    const int MOD = int(1e9) + 7;
    int d1[100001]; // num -> count
    int d2[100001]; // transition from d1[num * 2] to d2[num]

    memset(d1, 0, sizeof(d1));
    memset(d2, 0, sizeof(d2));

    ll total = 0;

    for (int num : nums) {
      if ((num & 1) == 0) {
        total = (total + d2[num / 2]) % MOD;
      }

      if (num <= 50000) { // out of bounds, not interested;
        d2[num] = (d2[num] + d1[num * 2]) % MOD;
      }

      d1[num]++;
    }

    return total;
  }
};