#include <vector>

using std::vector;

class Solution {
public:
  vector<int> separateDigits(vector<int> &nums) {
    vector<int> res;
    vector<int> digits;
    for (int num : nums) {
      while (num) {
        digits.push_back(num % 10);
        num /= 10;
      }

      while (digits.size()) {
        res.push_back(digits.back());
        digits.pop_back();
      }
    }

    return res;
  }
};