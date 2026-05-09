#include <string>

using std::string;

class Solution {
public:
  bool checkRecord(string s) {
    int a = 0, l = 0;

    for (char c : s) {
      if (c == 'A') {
        a++;
        l = 0;
      } else if (c == 'L') {
        l++;
      } else {
        l = 0;
      }

      if (a >= 2 || l >= 3) {
        return false;
      }
    }

    return true;
  }
};