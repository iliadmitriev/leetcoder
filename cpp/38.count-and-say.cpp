#include <string>

using std::string;

class Solution {
public:
  string countAndSay(int n) {
    string res = "1";

    for (n--; n; n--) {
      string tmp;

      int i = 0;

      while (i < res.size()) {
        char cur = res[i];
        int cnt = 0;

        while (i < res.size() && res[i] == cur) {
          i++;
          cnt++;
        }

        tmp.append(std::to_string(cnt));
        tmp.push_back(cur);
      }

      res = tmp;
    }

    return res;
  }
};