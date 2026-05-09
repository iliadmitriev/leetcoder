#include <string>

using std::string;

class Solution {
public:
  int countSegments(string s) {
    int seg = 0;
    char p = ' ';

    // count number of transitions from space to non-space
    for (char c : s) {
      if (p == ' ' && c != ' ') {
        seg++;
      }

      p = c;
    }

    return seg;
  }
};