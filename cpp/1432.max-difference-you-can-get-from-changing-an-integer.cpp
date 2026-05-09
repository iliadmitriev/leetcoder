#include <vector>
using std::vector;

class Solution {
public:
  int maxDiff(int num) {
    vector<int> value;

    while (num) {
      value.push_back(num % 10);
      num /= 10;
    }

    int aSrc = value.back(), aTar = 9;
    int bSrc = value.back(), bTar = 1;

    // find first non-9 from most significant to least significant
    for (int i = value.size() - 1; i >= 0; i--) {
      if (value[i] < 9) {
        aSrc = value[i];
        break;
      }
    }

    // if first is 1, then find next non-1 and non-0,
    // replace it with 0 if found
    if (bSrc == 1) {
      for (int i = value.size() - 1; i >= 0; i--) {
        if (value[i] > 1) {
          bTar = 0;
          bSrc = value[i];
          break;
        }
      }
    }

    int a = 0, b = 0;
    while (value.size()) {
      int v = value.back();
      value.pop_back();

      a *= 10;
      b *= 10;

      a += v == aSrc ? aTar : v;
      b += v == bSrc ? bTar : v;
    }

    return a - b;
  }
};