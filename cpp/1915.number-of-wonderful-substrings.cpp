#include <map>
#include <string>

using namespace std;

class Solution {
public:
  long long wonderfulSubstrings(string word) {
    long res = 0, mask = 0;

    map<int, int> cnt;
    cnt[0] = 1;
    for (auto ch : word) {
      mask ^= 1 << (ch - 'a');
      cnt[mask]++;
    }

    for (auto [mask, count] : cnt) {
      res += long(count) * (count - 1) / 2;
      for (int i = 0; i < 10; ++i) {
        int mask2 = mask ^ (1 << i);
        if (mask2 < mask) {
          res += long(count) * cnt[mask2];
        }
      }
    }

    return res;
  }
};