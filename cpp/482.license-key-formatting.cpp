#include <string>

using std::string;

class Solution {
public:
  string licenseKeyFormatting(string s, int k) {
    string tmp, res;
    tmp.reserve(s.size());
    res.reserve(s.size());

    int cnt = 0;

    for (char c : s) {
      if (c != '-') {
        tmp.push_back(std::toupper(c));
        cnt++;
      }
    }

    int rest = tmp.size() % k;
    if (rest == 0 && cnt > 0) {
      rest = k;
    }

    res.append(tmp.substr(0, rest));

    for (int i = rest; i < tmp.size(); i += k) {
      res.push_back('-');
      res.append(tmp.substr(i, k));
    }

    return res;
  }
};