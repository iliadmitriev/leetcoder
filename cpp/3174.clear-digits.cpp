#include <cctype>
#include <string>

using std::string;

class Solution {
public:
  string clearDigits(string s) {
    string res;

    for (char ch : s) {
      if (std::isalpha(ch)) {
        res.push_back(ch);
        continue;
      }

      if (!res.empty() && std::isalpha(res.back())) {
        res.pop_back();
      } else {
        res.push_back(ch);
      }
    }

    return res;
  }
};