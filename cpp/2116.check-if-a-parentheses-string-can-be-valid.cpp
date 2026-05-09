#include <iostream>
#include <string>
#include <vector>

using std::vector, std::string;

static const auto ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  bool canBeValid(string s, string locked) {
    vector<int> stack, freeStack;

    for (int i = 0; i < s.size(); i++) {
      if (locked[i] == '1') {
        if (s[i] == '(') {
          stack.push_back(i);
        } else {
          if (!stack.empty()) {
            stack.pop_back();
          } else if (!freeStack.empty()) {
            freeStack.pop_back();
          } else {
            return false;
          }
        }
      } else {
        freeStack.push_back(i);
      }
    }

    while (!stack.empty() && !freeStack.empty()) {
      if (stack.back() > freeStack.back()) {
        return false;
      }

      stack.pop_back();
      freeStack.pop_back();
    }

    return stack.empty() && freeStack.size() % 2 == 0;
  }
};