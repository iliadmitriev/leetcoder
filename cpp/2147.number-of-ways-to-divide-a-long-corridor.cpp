#include <string>
using std::string;

class Solution {
public:
  int numberOfWays(string corridor) {
    const int MOD = 1e9 + 7;
    int divider = 1;
    long res = 1;
    int seats = 0;

    for (char pos : corridor) {
      if (seats == 2) {
        if (pos == 'S') {
          seats = 1;
          res = (res * divider) % MOD;
          divider = 1;
        } else {
          divider++;
        }
      } else {
        if (pos == 'S') {
          seats++;
        }
      }
    }

    if (seats != 2) {
      return 0;
    }

    return res;
  }
};