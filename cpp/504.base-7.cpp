#include <string>
using std::string;

class Solution {
public:
  string convertToBase7(int num) {
    if (!num) {
      return "0";
    }

    bool sign = num < 0;
    num = sign ? -num : num;

    string res;
    while (num) {
      res.push_back(num % 7 + '0');
      num /= 7;
    }

    if (sign) {
      res.push_back('-');
    }

    std::reverse(res.begin(), res.end());

    return res;
  }
};