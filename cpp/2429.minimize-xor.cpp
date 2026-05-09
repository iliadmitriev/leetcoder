
class Solution {
public:
  int minimizeXor(int num1, int num2) {
    int bits1 = __builtin_popcount(num1);
    int bits2 = __builtin_popcount(num2);

    int res = num1;

    if (bits1 > bits2) {
      int remove = bits1 - bits2;
      for (int i = 1; remove; i <<= 1) {
        if (res & i) {
          res ^= i;
          remove--;
        }
      }
    } else if (bits2 > bits1) {
      int add = bits2 - bits1;

      for (int i = 1; add; i <<= 1) {
        if ((res & i) == 0) {
          res |= i;
          add--;
        }
      }
    }

    return res;
  }
};