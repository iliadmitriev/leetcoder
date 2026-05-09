#include <string>

using std::string;

class Solution {
private:
  string stacker(const string &s) {
    string stack;
    for (auto c : s) {
      if (c != '#') {
        stack.push_back(c);
      } else if (!stack.empty()) {
        stack.pop_back();
      }
    }
    return stack;
  }

public:
  bool backspaceCompare(string s, string t) {
    string s1 = stacker(s);
    string s2 = stacker(t);
    return s1 == s2;
  }
};