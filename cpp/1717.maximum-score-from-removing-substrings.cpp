#include <string>
using std::string;

class Solution {
private:
  int getMax(string s, char cha, char chb, int x, int y) {
    int c1 = 0, c2 = 0, res = 0;

    for (char c : s) {
      if (c == cha) {
        c1++;
      } else if (c == chb) {
        if (c1 > 0) {
          c1--;
          res += x;
        } else {
          c2++;
        }
      } else {
        res += y * std::min(c1, c2);
        c1 = 0;
        c2 = 0;
      }
    }

    // add remaining
    res += y * std::min(c1, c2);

    return res;
  }

public:
  int maximumGain(string s, int x, int y) {
    if (x > y) {
      return getMax(s, 'a', 'b', x, y);
    } else {
      return getMax(s, 'b', 'a', y, x);
    }
  }
};