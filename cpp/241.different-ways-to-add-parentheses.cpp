#include <cctype>
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
private:
  int inline applyOp(char op, int a, int b) {
    if (op == '+') {
      return a + b;
    } else if (op == '-') {
      return a - b;
    }
    // else op == '*'
    return a * b;
  }

public:
  vector<int> diffWaysToCompute(string expression) {
    if (!expression.size()) {
      return {};
    }

    if (expression.size() == 1) {
      return {std::stoi(expression)};
    }

    if (expression.size() == 2 && std::isdigit(expression[0]) &&
        std::isdigit(expression[1])) {
      return {std::stoi(expression)};
    }

    vector<int> result;

    for (int i = 0; i < expression.size(); i++) {
      if (std::isdigit(expression[i])) {
        continue;
      }

      vector<int> leftResult = diffWaysToCompute(expression.substr(0, i));
      vector<int> rightResult = diffWaysToCompute(expression.substr(i + 1));

      for (int left : leftResult) {
        for (int right : rightResult) {
          result.push_back(applyOp(expression[i], left, right));
        }
      }
    }

    return result;
  }
};