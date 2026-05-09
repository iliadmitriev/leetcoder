#include <vector>
using std::vector;

class Solution {
public:
  int numOfSubarrays(vector<int> &arr) {
    int odd = 0, even = 0;
    int cur = 0;

    for (int num : arr) {
      cur += num;
      if (cur % 2) {
        odd++;
      } else {
        even++;
      }
    }

    return long(1 + even) * long(odd) % int(1e9 + 7);
  }
};