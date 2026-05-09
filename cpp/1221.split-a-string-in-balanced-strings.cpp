#include <string>
using std::string;

class Solution {
public:
  int balancedStringSplit(string s) {
    int res = 0, balance = 0;

    for (char c : s) {
      balance += c == 'L' ? 1 : -1;
      res += balance == 0;
    }

    return res;
  }
};