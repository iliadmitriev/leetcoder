#include <string>
using std::string;

class Solution {
public:
  string thousandSeparator(int n) {
    if (n == 0) {
      return "0";
    }
    string res;
    int count = 0;

    while (n) {
      res.push_back('0' + n % 10);
      n /= 10;
      count++;

      if (count == 3 && n) {
        count = 0;
        res.push_back('.');
      }
    }

    std::reverse(res.begin(), res.end());
    return res;
  }
};