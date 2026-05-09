#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  bool isAcronym(vector<string> &words, string s) {
    if (s.size() != words.size()) {
      return false;
    }

    for (int i = 0; i < words.size(); i++) {
      if (words[i].empty() || words[i][0] != s[i]) {
        return false;
      }
    }
    return true;
  }
};