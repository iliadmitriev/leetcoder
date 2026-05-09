class Solution {
public:
  int makeTheIntegerZero(int num1, int num2) {

    long x;
    for (int k = 1; k < 33; k++) {
      long x = num1 - long(num2) * k;

      if (x < k) {
        return -1;
      }

      // WARNING: popcount for long !!
      if (__builtin_popcountll(x) <= k) {
        return k;
      }
    }

    return -1;
  }
};