class Solution {
public:
  char findKthBit(int n, int k) {
    if (n == 0)
      return '0';

    int mid = (1 << (n - 1)) - 1;
    int inv = 0;
    k--;

    while (k > 0) {
      if (k > mid) {
        k = 2 * mid - k;
        inv++;
      }

      mid /= 2;
    }

    if (inv % 2) {
      return '1';
    }

    return '0';
  }
};