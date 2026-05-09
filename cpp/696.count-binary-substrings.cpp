#include <string>
using std::string;

class Solution {
public:
  int countBinarySubstrings(string s) {
    int a = 0, b = 0, count = 0;
    char prev = '#';

    for (char c : s) {
      if (c == prev) {
        a++;
      } else {
        count += std::min(a, b);
        b = a, a = 1;
      }

      prev = c;
    }

    return count + std::min(a, b);
  }
};