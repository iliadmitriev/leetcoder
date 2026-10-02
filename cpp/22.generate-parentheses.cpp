#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
      vector<string> res;

      auto dp = [&res](const auto& self, int opening, int closing, string s) {
        if (opening == 0 && closing == 0) {
          res.push_back(s);
          return;
        }

        if (opening > closing) {
          return;
        }

        if (opening) {
          self(self, opening - 1, closing, s + "(");
        }

        if (closing) {
          self(self, opening, closing - 1, s + ")");
        }
      };

      dp(dp, n, n, "");

      return res;  
    }
};