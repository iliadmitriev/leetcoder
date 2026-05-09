#include <queue>
#include <vector>

using std::vector, std::priority_queue;

class Solution {
public:
  int largestPerimeter(vector<int> &nums) {
    priority_queue<int> hq(nums.begin(), nums.end());

    while (hq.size() >= 3) {
      int a = hq.top();
      hq.pop();
      int b = hq.top();
      hq.pop();
      int c = hq.top();

      if (b + c > a) {
        return a + b + c;
      }

      hq.push(b);
    }

    return 0;
  }
};