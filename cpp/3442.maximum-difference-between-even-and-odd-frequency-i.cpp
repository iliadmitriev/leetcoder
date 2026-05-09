#include <array>
#include <string>
using std::string, std::array;

class Solution {
public:
  int maxDifference(string s) {
    array<int, 26> cnt = {0};
    int a1 = 0, a2 = INT_MAX;

    for (char c : s) {
      cnt[c - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
      if (cnt[i] == 0) {
        continue;
      }

      if (cnt[i] % 2) {
        a1 = std::max(a1, cnt[i]);
      } else {
        a2 = std::min(a2, cnt[i]);
      }
    }

    return a1 - a2;
  }
};