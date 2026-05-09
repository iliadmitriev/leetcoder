#include <vector>
using std::vector;

class Solution {
public:
  int maximumLength(vector<int> &nums) {
    int odd = 0, even = 0, alter1 = 0, alter2 = 0;

    for (int num : nums) {
      if (num % 2 == 0) {
        even++;
        alter1 = 1 + alter2;
      } else {
        odd++;
        alter2 = 1 + alter1;
      }
    }

    return std::max(std::max(even, odd), std::max(alter1, alter2));
  }
};