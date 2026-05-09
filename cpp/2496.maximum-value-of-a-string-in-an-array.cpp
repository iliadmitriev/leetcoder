#include <cctype>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  bool inline isDigit(const string &s) {
    for (char c : s) {
      if (!std::isdigit(c)) {
        return false;
      }
    }

    return true;
  }

public:
  int maximumValue(vector<string> &strs) {
    int maxLen = 0;

    for (const string &s : strs) {
      int curLen = s.size();
      if (isDigit(s)) {
        curLen = std::atoi(s.c_str());
      }

      maxLen = std::max(maxLen, curLen);
    }

    return maxLen;
  }
};