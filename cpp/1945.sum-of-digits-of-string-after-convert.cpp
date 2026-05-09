#include <string>

using std::string;

class Solution {
public:
  int getLucky(string s, int k) {
    string num;

    for (char ch : s) {
      num += std::to_string(ch - 'a' + 1);
    }

    while (k--) {
      int digits = 0;
      for (char ch : num) {
        digits += ch - '0';
      }

      num = std::to_string(digits);
    }

    return std::stoi(num);
  }
};