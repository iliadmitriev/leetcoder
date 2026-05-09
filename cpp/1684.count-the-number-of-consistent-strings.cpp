#include <ios>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  int bitmask(const string &s) {
    int res = 0;

    for (char ch : s) {
      res |= 1 << (ch - 'a');
    }

    return res;
  }

public:
  int countConsistentStrings(string allowed, vector<string> &words) {
    // speedup
    std::ios_base::sync_with_stdio(false);

    int forbiddenMask = ~bitmask(allowed);
    int count = 0;

    for (string &word : words) {
      int wordMask = bitmask(word);

      if (!(wordMask & forbiddenMask)) {
        count++;
      }
    }

    return count;
  }
};