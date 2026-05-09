#include <vector>
using std::vector;

class Solution {
public:
  bool canArrange(vector<int> &arr, int k) {
    int *freq;
    freq = new int[k];
    memset(freq, 0, sizeof(int) * k);

    for (int num : arr) {
      freq[(num % k + k) % k]++;
    }

    if (freq[0] % 2 != 0) {
      return false;
    }

    if (k % 2 == 0 && freq[k / 2] % 2 != 0) {
      return false;
    }

    for (int i = 1; i <= k / 2; i++) {
      if (freq[i] != freq[k - i]) {
        return false;
      }
    }

    return true;
  }
};