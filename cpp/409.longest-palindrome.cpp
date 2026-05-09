#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int longestPalindrome(string s) {
    int res = 0, mid = 0;
    const int N = 58;

    vector<int> cnt(N, 0);
    for (const char &c : s) {
      cnt[c - 'A']++;
    }

    for (int i = 0; i < N; ++i) {
      res += cnt[i] - cnt[i] % 2;
      mid |= cnt[i] % 2;
    }

    return res + mid;
  }
};