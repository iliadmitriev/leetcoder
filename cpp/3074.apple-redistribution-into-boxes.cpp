#include <algorithm>
#include <numeric>
#include <vector>

using std::vector;

class Solution {
public:
  int minimumBoxes(vector<int> &apple, vector<int> &capacity) {
    std::sort(capacity.rbegin(), capacity.rend());
    int totalApples = std::accumulate(apple.begin(), apple.end(), 0);
    int count = 0;

    for (int cap : capacity) {
      totalApples -= cap;
      count++;

      if (totalApples <= 0)
        break;
    }

    return count;
  }
};