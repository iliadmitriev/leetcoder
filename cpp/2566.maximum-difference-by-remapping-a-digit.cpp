#include <vector>
using std::vector;

class Solution {
public:
  int minMaxDifference(int num) {
    vector<int> digits;
    while (num) {
      digits.push_back(num % 10);
      num /= 10;
    }

    int aSrc = digits.back(), aTar = 9;
    int bSrc = digits.back(), bTar = 0;

    // find first non-9 from most significant to least significant
    for (int i = digits.size() - 1; i >= 0; i--) {
      if (digits[i] < 9) {
        aSrc = digits[i];
        break;
      }
    }

    int a = 0, b = 0;

    while (digits.size()) {
      int v = digits.back();
      digits.pop_back();

      a *= 10;
      b *= 10;

      a += v == aSrc ? aTar : v;
      b += v == bSrc ? bTar : v;
    }

    return a - b;
  }
};