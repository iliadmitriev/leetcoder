#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  string largestNumber(vector<int> &nums) {
    vector<string> numStr;
    for (int num : nums) {
      numStr.push_back(std::to_string(num));
    }

    std::sort(numStr.begin(), numStr.end(),
              [](const string &a, const string &b) { return a + b > b + a; });

    if (numStr[0] == "0") {
      return "0";
    }

    std::stringstream res;
    for (const string &num : numStr) {
      res << num;
    }

    return res.str();
  }
};