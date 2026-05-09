#include <string>

using std::string;

class Solution {
public:
  int appendCharacters(string s, string t) {
    int j = 0;
    int m = s.size(), n = t.size();

    for (int i = 0; i < m && j < n; i++) {
      if (t[j] == s[i]) {
        j++;
      }
    }

    return n - j;
  }
};