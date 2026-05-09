#include <climits>

class Solution {
public:
  int smallestNumber(int n) {
    int len = sizeof(int) * CHAR_BIT - __builtin_clz(n);
    return (1 << len) - 1;
  }
};