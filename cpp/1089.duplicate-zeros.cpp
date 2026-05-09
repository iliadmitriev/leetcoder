#include <ios>
#include <vector>
using std::vector;

class Solution {
public:
  void duplicateZeros(vector<int> &arr) {
    std::ios_base::sync_with_stdio(false);

    int n = arr.size();

    int zeros = 0;
    for (int n : arr) {
      if (n == 0) {
        zeros++;
      }
    }

    for (int i = n - 1, j = n + zeros - 1; i >= 0 && j > i; --i, --j) {
      if (j < n) {
        arr[j] = arr[i];
      }

      if (arr[i] == 0 && --j < n) {
        arr[j] = 0;
      }
    }
  }
};