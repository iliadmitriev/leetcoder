#include <iostream>
#include <vector>

static const auto io_sync_off = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return nullptr;
}();

using std::vector;

class Solution {
public:
  int numberOfAlternatingGroups(vector<int> &colors, int k) {
    const int n = colors.size();
    const int m = n + k - 1;
    int curAlt = 1, alt = 0;

    for (int i = 1; i < m; i++) {
      if (colors[(i - 1) % n] == colors[i % n]) {
        curAlt = 1;
        continue;
      }

      curAlt++;
      alt += (curAlt >= k);
    }

    return alt;
  }
};