#include <functional>
#include <queue>
#include <utility>
#include <vector>
using std::vector, std::priority_queue, std::max, std::greater, std::pair;

class Solution {
public:
  vector<int> smallestRange(vector<vector<int>> &nums) {
    int n = nums.size();
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;

    vector<int> inx(n, 0);
    int right = nums[0][0];

    for (int i = 0; i < n; i++) {
      minHeap.push({nums[i][inx[i]], i});
      right = max(right, nums[i][inx[i]]);
      inx[i]++;
    }

    vector<int> res = {minHeap.top().first, right};
    int curDiff = right - minHeap.top().first;

    while (minHeap.size()) {
      auto [left, i] = minHeap.top();
      minHeap.pop();

      if (right - left < curDiff) {
        curDiff = right - left;
        res[0] = left, res[1] = right;
      }

      if (inx[i] == nums[i].size()) {
        break;
      }

      minHeap.push({nums[i][inx[i]], i});
      right = max(right, nums[i][inx[i]]);
      inx[i]++;
    }

    return res;
  }
};