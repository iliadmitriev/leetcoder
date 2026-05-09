#include <sstream>
#include <string>
#include <utility>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  int gcd(int a, int b) {
    int t;
    while (b) {
      t = b;
      b = a % b;
      a = t;
    }
    return a;
  }

public:
  string fractionAddition(string expression) {
    vector<std::pair<int, int>> frac;
    std::istringstream iss(expression);

    int num = 0, den = 0;
    char _;

    while (iss >> num >> _ >> den) {
      frac.push_back({num, den});
    }

    num = 0, den = 1;
    for (auto &[_num, _den] : frac) {
      num = num * _den + _num * den;
      den *= _den;
    }

    if (num == 0)
      return "0/1";

    int g = gcd(abs(num), den);
    num /= g;
    den /= g;

    std::stringstream res;
    res << num << "/" << den;
    return res.str();
  }
};