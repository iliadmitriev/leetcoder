#include <string>
#include <numeric>
using std::string;


class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
      int pos = 0, spc = 0;

      for (char m : moves) {
        if (m == 'L') {
          pos--;
        } else if (m == 'R') {
          pos++;
        } else {
          spc++;
        }
      }

      return std::abs(pos) + spc;
    }
};