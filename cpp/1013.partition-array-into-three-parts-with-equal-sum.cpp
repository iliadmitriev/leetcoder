#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  bool canThreePartsEqualSum(vector<int> &arr) {
    int total = std::accumulate(arr.begin(), arr.end(), 0);

    if (total % 3) {
      return false;
    }

    int partial = total / 3;
    int sum = 0;
    int state = 0;

    for (int num : arr) {
      sum += num;

      if (sum == partial) {
        state++;
        sum = 0;
      }

      if (state == 3) {
        return true;
      }
    }

    return false;
  }
};