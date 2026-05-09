#include <vector>

using std::vector;

class Solution {
public:
  double calculateTax(vector<vector<int>> &brackets, int income) {
    double tax = 0.0;
    int prevBase = 0;

    for (const auto &bracket : brackets) {
      int base = std::min(income, bracket[0] - prevBase);
      int rate = bracket[1];

      tax += base * rate / 100.0;
      income -= base;
      prevBase = bracket[0];

      if (income == 0) {
        break;
      }
    }

    return tax;
  }
};