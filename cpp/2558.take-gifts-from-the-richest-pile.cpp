#include <iostream>
#include <queue>
#include <vector>

using std::priority_queue;
using std::vector;

static const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
  long long pickGifts(vector<int> &gifts, int k) {
    priority_queue<int> q(gifts.begin(), gifts.end());

    for (; k; k--) {
      // optimize
      if (q.top() == 1)
        break;
      int res = std::sqrt(q.top());
      q.pop();
      q.push(res);
    }

    long long res = 0;

    const int *base = &q.top();
    for (size_t i = 0; i < q.size(); i++, base++) {
      res += *base;
    }

    return res;
  }
};