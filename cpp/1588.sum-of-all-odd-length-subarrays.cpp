#include <vector>

using std::vector;

class Solution {
public:
  int sumOddLengthSubarrays(vector<int> &arr) {
    int res = 0;

    int n = arr.size();

    // convolution k * (n - k- 1)
    // number of all occurences of the array item in every contiguous subarray
    // shift left by +1
    // (k + 1) * (n - k) + 1
    // divide it by 2 (take only odd)
    // ((k + 1) * (n - k) + 1) / 2

    for (int i = 0; i < n; i++) {
      res += ((i + 1) * (n - i) + 1) / 2 * arr[i];
    }

    return res;
  }
};