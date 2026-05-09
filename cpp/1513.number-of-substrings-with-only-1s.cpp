#include <string>
using std::string;

const int MOD = 1e9 + 7;

class Solution {
private:
  long long count(long long n) { return n * (n + 1) / 2; }

public:
  int numSub(string s) {
    long long ret = 0;

    int cur = 0;

    for (char ch : s) {
      if (ch == '1') {
        cur++;
      } else {
        ret += count(cur);
        ret %= MOD;
        cur = 0;
      }
    }

    ret += count(cur);
    ret %= MOD;

    return ret;
  }
};