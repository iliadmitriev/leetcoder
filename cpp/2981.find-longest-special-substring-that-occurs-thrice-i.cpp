#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  int maximumLength(string s) {
    int lo = 0, hi = s.size(), mid;
    int result = 0;

    while (lo < hi) {
      mid = (lo + hi) / 2;
      if (check(s, mid)) {
        lo = mid + 1;
        result = mid;
      } else {
        hi = mid;
      }
    }

    if (result == 0) {
      return -1;
    }

    return result;
  }

private:
  bool check(const string &s, int len) {
    if (len == 0) {
      return true;
    }

    const int n = s.size();
    vector<int> count(26, 0);

    for (int i = 0; i < n - len + 1; i++) {
      char key = s[i];
      if (!same(s, i, i + len)) {
        continue;
      }

      count[key - 'a']++;

      if (count[key - 'a'] == 3) {
        return true;
      }
    }

    return false;
  }

  bool same(const string &s, int l1, int l2) {
    char key = s[l1];
    for (int i = l1; i < l2; i++) {
      if (s[l1] != s[i]) {
        return false;
      }
    }
    return true;
  }
};