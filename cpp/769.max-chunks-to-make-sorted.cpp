#include <vector>
using std::vector;

class Solution {
public:
  int maxChunksToSorted(vector<int> &arr) {
    int curMax = -1;
    int chunks = 0;

    for (int i = 0; i < arr.size(); i++) {
      if (curMax < arr[i]) {
        curMax = arr[i];
      }

      if (i == curMax) {
        chunks++;
      }
    }

    return chunks;
  }
};