#include <algorithm>
#include <vector>
using std::vector;

class Solution {
public:
  int findLengthOfShortestSubarray(vector<int> &arr) {
    const int n = arr.size();
    int i = 0, j = n - 1;

    while (i < j && arr[i] <= arr[i + 1]) {
      i++;
    }

    if (i == n - 1) {
      return 0;
    }

    int minLen = n - i - 1;

    while (i < j && arr[j - 1] <= arr[j]) {
      j--;
    }

    minLen = std::min(minLen, j);

    int left = i;
    i = 0;

    while (i <= left && j < n) {
      if (arr[i] <= arr[j]) {
        minLen = std::min(minLen, j - i - 1);
        i++;
      } else {
        j++;
      }
    }

    return minLen;
  }
};