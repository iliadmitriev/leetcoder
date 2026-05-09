#include <vector>
using std::vector;

class Solution {
public:
  bool isOneBitCharacter(vector<int> &bits) {
    int n = bits.size();

    for (int i = 0; i < n; i += (1 + bits[i])) {
      if (i == n - 1) {
        return true;
      }
    }

    return false;
  }
};