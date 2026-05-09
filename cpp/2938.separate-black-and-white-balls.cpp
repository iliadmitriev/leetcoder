#include <string>
using std::string;
class Solution {
public:
  long long minimumSteps(string s) {
    long long swaps = 0;

    for (int i = 0, j = s.size() - 1; i < j; i++, j--) {
      while (i < j && s[i] == '0')
        i++;

      while (i < j && s[j] == '1')
        j--;

      swaps += j - i;
    }

    return swaps;
  }
};