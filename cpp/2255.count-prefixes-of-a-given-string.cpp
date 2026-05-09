#include <cstring>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  bool inline startsWith(const string &s, const string &t) {
    return s.size() >= t.size() && strncmp(s.c_str(), t.c_str(), t.size()) == 0;
  }

public:
  int countPrefixes(vector<string> &words, string s) {
    int count = 0;

    for (const string &word : words) {
      if (startsWith(s, word)) {
        count++;
      }
    }

    return count;
  }
};