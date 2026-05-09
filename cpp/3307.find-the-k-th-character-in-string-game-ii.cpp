#include <vector>
using std::vector;

class Solution {
private:
  // count bit length of x long (64 bit)
  // using count leading zeros
  inline int length(long long x) {
    return (x == 0) ? 0 : 64 - __builtin_clzll(x);
  }

public:
  char kthCharacter(long long k, vector<int> &operations) {
    int res = 0;
    k--;

    while (k) {
      int t = length(k) - 1;
      k -= 1L << t;
      res += operations[t];
    }

    return 'a' + res % 26;
  }
};