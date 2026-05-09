#include <algorithm>
#include <string>
using std::string;

class Solution {
public:
  string addStrings(string num1, string num2) {
    const int m = num1.size(), n = num2.size();
    const int k = std::max(m, n);

    string res;
    res.reserve(k + 1);
    int carry = 0;

    for (int i = 0; i < k; i++) {
      int x = i < m ? num1[m - i - 1] - '0' : 0;
      int y = i < n ? num2[n - i - 1] - '0' : 0;

      int sum = x + y + carry;
      carry = sum / 10;
      res.push_back(sum % 10 + '0');
    }

    if (carry) {
      res.push_back(carry + '0');
    }

    std::reverse(res.begin(), res.end());

    return res;
  }
};