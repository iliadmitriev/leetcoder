#include <algorithm>
#include <string>
using std::string;

class Solution {
public:
  bool doesAliceWin(string s) {
    return std::any_of(s.begin(), s.end(), [](char c) {
      return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    });
  }
};