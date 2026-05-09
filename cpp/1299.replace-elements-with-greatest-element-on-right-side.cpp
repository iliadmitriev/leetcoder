#include <vector>

using std::vector;

class Solution {
public:
  vector<int> replaceElements(vector<int> &arr) {
    int maxRight = -1;
    for (int i = arr.size() - 1; i >= 0; i--) {
      int temp = arr[i];
      arr[i] = maxRight;
      maxRight = std::max(maxRight, temp);
    }

    return arr;
  }
};