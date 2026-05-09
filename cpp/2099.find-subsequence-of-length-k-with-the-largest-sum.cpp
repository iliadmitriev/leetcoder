#include <functional>
#include <queue>
#include <utility>
#include <vector>

using std::vector, std::priority_queue, std::pair, std::greater;

class Solution {
public:
  vector<int> maxSubsequence(vector<int> &nums, int k) {
    typedef pair<int, int> P; // <value, index>
    priority_queue<P, vector<P>, greater<>> hq;

    for (int i = 0; i < nums.size(); i++) {
      if (hq.size() < k) {
        hq.push({nums[i], i});
      } else {
        if (nums[i] > hq.top().first) {
          hq.pop();
          hq.push({nums[i], i});
        }
      }
    }

    // iterate over heap container without poping elements and modifying
    // access to underlying container, which is a vector
    vector<P> tmp(hq.size());
    const P *base = &hq.top();
    for (size_t i = 0; i < hq.size(); i++)
      tmp[i] = *(base + i);

    std::sort(tmp.begin(), tmp.end(),
              [](P a, P b) { return a.second < b.second; });

    vector<int> result(k);
    for (int i = 0; i < k; i++) {
      result[i] = nums[tmp[i].second];
    }
    return result;
  }
};