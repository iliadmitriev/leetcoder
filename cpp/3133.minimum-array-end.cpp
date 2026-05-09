class Solution {
public:
  long long minEnd(int n, int x) {
    long long mask = x, num = n - 1;
    int i = 0;

    while (num) {
      if ((x & 1) == 0) {
        mask |= (num & 1) << i;
        num >>= 1;
      }

      x >>= 1;
      i++;
    }

    return mask;
  }
};