#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
private:
  string backtrack(const string &pattern, vector<bool> used, int idx,
                   string cur) {

    if (idx == pattern.size() + 1) {
      return cur;
    }

    int start = 1, end = 9;
    if (idx > 0) {
      if (pattern[idx - 1] == 'I') {
        start = cur.back() - '0' + 1;
      } else {
        end = cur.back() - '0' - 1;
      }
    }

    for (int i = start; i <= end; i++) {
      if (used[i]) {
        continue;
      }

      used[i] = true;
      string res = backtrack(pattern, used, idx + 1, cur + std::to_string(i));
      used[i] = false;

      if (res.size() > 0) {
        return res;
      }
    }

    return "";
  }

public:
  string smallestNumber(string pattern) {
    return backtrack(pattern, vector(10, false), 0, "");
  }
};