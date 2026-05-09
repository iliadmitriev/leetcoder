#include <ios>
#include <iostream>
#include <queue>
#include <unordered_set>
#include <utility>
#include <vector>

using std::vector, std::unordered_set, std::priority_queue, std::pair;

const static int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  long long findScore(vector<int> &nums) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<>> pq;
    for (int i = 0; i < nums.size(); i++) {
      pq.push({nums[i], i});
    }

    unordered_set<int> marked;
    long long score = 0;

    while (!pq.empty()) {
      auto [val, idx] = pq.top();
      pq.pop();

      if (marked.count(idx)) {
        continue;
      }

      score += val;
      marked.insert(idx);
      marked.insert(idx - 1);
      marked.insert(idx + 1);
    }

    return score;
  }
};