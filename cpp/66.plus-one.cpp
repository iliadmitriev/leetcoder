#include <vector>
using std::vector;

class Solution {
public:
  vector<int> plusOne(vector<int> &digits) {
    int carry = 1;
    int tmp;

    for (int n = digits.size() - 1; n >= 0 && carry; n--) {
      tmp = carry + digits[n];
      carry = tmp / 10;
      digits[n] = tmp % 10;
    }

    if (carry) {
      digits.insert(digits.begin(), 1);
    }

    return digits;
  }
};