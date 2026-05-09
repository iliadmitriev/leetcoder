#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int finalPositionOfSnake(int n, vector<string> &commands) {

    int r = 0, c = 0;

    for (const string &cmd : commands) {
      switch (cmd[0]) {
      case 'R':
        c++;
        break;
      case 'L':
        c--;
        break;
      case 'U':
        r--;
        break;
      case 'D':
        r++;
        break;
      }
    }

    return r * n + c;
  }
};