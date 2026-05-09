#include <string>
using std::string;

class Solution {
public:
  int longestSubsequence(string s, int k) {
    const int n = s.size();
    int curLen = 0, curVal = 0;
    int zerosLeft = std::count(s.begin(), s.end(), '0');

    for (int i = n - 1; i >= 0; i--) {
      if (s[i] == '0') {
        zerosLeft--;
      } else {
        if (curLen <= 30) {
          curVal += 1 << curLen;
        } else {
          return curLen + zerosLeft;
        }
      }

      if (curVal > k) {
        return curLen + zerosLeft;
      }

      curLen++;
    }

    return n;
  }
};