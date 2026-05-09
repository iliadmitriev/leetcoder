class Solution {
public:
  int numTilings(int n) {
    const int MOD = 1e9 + 7;
    long f = 1, f1 = 1, f2 = 1, f3 = 0;

    for (int i = 1; i < n; ++i) {
      f = (2 * f1 + f3) % MOD;
      f3 = f2;
      f2 = f1;
      f1 = f;
    }

    return f;
  }
};