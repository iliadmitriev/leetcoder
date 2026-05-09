#include <vector>
using std::vector;

class Solution {
public:
  vector<int> getSneakyNumbers(vector<int> &nums) {
    vector<int> sneaky;

    const int n = nums.size();
    vector<int> cache(n - 2, 0);

    for (int num : nums) {
      if (cache[num]) {
        sneaky.push_back(num);
      }
      cache[num]++;
    }

    return sneaky;
  }
};