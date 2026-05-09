#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  vector<string> divideString(string s, int k, char fill) {
    const int n = s.size();
    vector<string> res;
    res.reserve(n / k + 1);

    for (int i = 0; i < n; i += k) {
      res.push_back(s.substr(i, k));
    }

    while (res.back().size() < k) {
      res.back().push_back(fill);
    }

    return res;
  }
};