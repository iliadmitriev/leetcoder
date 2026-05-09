#include <vector>
using std::vector;

const int MOD = 1e9 + 7;

class Solution {
private:
  int pow(int base, int exponent, int mod) {
    if (mod == 1) {
      return 0;
    }
    long res = 1;
    base %= mod;
    while (exponent > 0) {
      if (exponent % 2) {
        res = (res * base) % mod;
      }
      exponent >>= 1;
      base = (long(base) * base) % mod;
    }
    return int(res);
  }

public:
  int numSubseq(vector<int> &nums, int target) {
    int i = 0, j = nums.size() - 1;
    long long total = 0;

    std::sort(nums.begin(), nums.end());

    while (i <= j) {
      if (nums[i] + nums[j] <= target) {
        total += pow(2, (j - i), MOD);
        i++;
      } else {
        j--;
      }
    }

    return total % MOD;
  }
};