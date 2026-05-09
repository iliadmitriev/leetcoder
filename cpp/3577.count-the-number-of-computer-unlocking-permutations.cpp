#include <vector>
using std::vector;

class Solution {
public:
  int countPermutations(vector<int> &complexity) {
    const int n = complexity.size();
    const int lowest = complexity.front();

    for (int i = 1; i < n; i++) {
      if (complexity[i] <= lowest) {
        return 0;
      }
    }

    typedef long long LL;
    const LL mod = 1e9 + 7;
    LL perm = 1;

    for (int i = 2; i < n; i++) {
      perm = perm * i % mod;
    }

    return perm;
  }
};