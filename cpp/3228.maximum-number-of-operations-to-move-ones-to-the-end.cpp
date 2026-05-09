#include <string>
using std::string;

class Solution {
public:
  int maxOperations(string s) {
    int inc = 0, cnt = 0;
    char p = '1';

    for (int i = s.size(); i >= 0; i--) {
      if (p != '0' && s[i] == '0') {
        inc++;
      } else if (s[i] == '1') {
        cnt += inc;
      }

      p = s[i];
    }

    return cnt;
  }
};