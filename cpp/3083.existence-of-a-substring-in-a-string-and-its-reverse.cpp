#include <string>
#include <unordered_set>

using std::string;
using std::unordered_set;

class Solution {
public:
  bool isSubstringPresent(string s) {
    unordered_set<string> r;
    string t(s.rbegin(), s.rend());

    for (int i = 0; i < t.size() - 1; i++) {
      r.insert(t.substr(i, 2));
    }

    for (int i = 0; i < s.size() - 1; i++) {
      if (r.count(s.substr(i, 2))) {
        return true;
      }
    }

    return false;
  }
};