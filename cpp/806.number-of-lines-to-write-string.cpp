#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  vector<int> numberOfLines(vector<int> &widths, string s) {
    int pixels = 0, lines = 1;

    for (char ch : s) {
      if (pixels + widths[ch - 'a'] > 100) {
        pixels = 0;
        ++lines;
      }

      pixels += widths[ch - 'a'];
    }

    return {lines, pixels};
  }
};