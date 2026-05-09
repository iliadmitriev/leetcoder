
class Solution {
public:
  int minBitFlips(int start, int goal) {
    start ^= goal;
    int n = 0;

    while (start) {
      n += start & 1;
      start >>= 1;
    }
    return n;
  }
};