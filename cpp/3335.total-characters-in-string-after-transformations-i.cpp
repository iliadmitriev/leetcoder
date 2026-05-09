#include <array>
#include <string>

using std::array, std::string;

class Solution {
public:
  int lengthAfterTransformations(string s, int t) {
    const int N = 'z' - 'a' + 1;
    const int MOD = 1e9 + 7;

    int full = t / N, extra = t % N;
    long res = 0;
    array<int, N> cnt = {0};

    for (char c : s) {
      cnt[c - 'a']++;
    }

    while (full--) {
      int tmp = cnt[N - 1];
      for (int i = N - 1; i > 0; i--) {
        cnt[i] = (cnt[i] + cnt[i - 1]) % MOD;
      }
      cnt[0] = (cnt[0] + tmp) % MOD;
      cnt[1] = (cnt[1] + tmp) % MOD;
    }

    for (int i = N - 1; i >= N - extra; i--) {
      cnt[i] = (cnt[i] + cnt[i]) % MOD;
    }

    for (int i = 0; i < N; i++) {
      res = (res + cnt[i]) % MOD;
    }

    return res;
  }
};