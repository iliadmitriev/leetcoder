#include <string>

using std::string;

class Solution {
public:
  int minimumRecolors(string blocks, int k) {
    int count = k, curWindow = 0;

    for (int i = 0; i < blocks.size(); ++i) {
      if (blocks[i] == 'W')
        ++curWindow;

      if (i >= k && blocks[i - k] == 'W')
        --curWindow;

      if (i >= k - 1)
        count = std::min(count, curWindow);
    }

    return count;
  }
};