#include <vector>
using std::vector;

class Solution {
public:
  int numberOfAlternatingGroups(vector<int> &colors) {
    int n = colors.size();
    int count = 0;

    for (int i = 0; i < n; i++) {
      if (colors[i] != colors[(n + i - 1) % n] &&
          colors[i] != colors[(i + 1) % n]) {
        count++;
      }
    }

    return count;
  }
};