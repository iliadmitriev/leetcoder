#include <cmath>
class Solution {
public:
  int countTriples(int n) {
    int count = 0;

    for (int i = 1; i <= n; i++) {
      for (int j = i; j <= n; j++) {
        int v = i * i + j * j;
        int r = std::sqrt(v);

        if (r > n) {
          break;
        }

        if (r * r == v) {
          count++;
        }
      }
    }

    return count * 2;
  }
};