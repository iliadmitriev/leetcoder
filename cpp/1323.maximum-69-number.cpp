#include <cmath>

class Solution {
public:
  int maximum69Number(int num) {
    int pos = -1;

    for (int x = num, i = 0; x > 0; x /= 10, i++) {
      if (x % 10 == 6) {
        pos = i; // don't break on first match, go on to find most significant
                 // digit 6
      }
    }

    if (pos == -1) {
      return num;
    }

    return num + (3 * std::pow(10, pos));
  }
};