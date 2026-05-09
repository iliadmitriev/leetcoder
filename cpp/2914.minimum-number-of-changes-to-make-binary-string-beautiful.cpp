#include <string>
using std::string;

class Solution {
public:
  int minChanges(string s) {
    int n = s.size(), counter = 0;

    for (int i = 0; i < n; i += 2) {
      counter += (s[i] != s[i + 1]);
    }

    return counter;
  }
};