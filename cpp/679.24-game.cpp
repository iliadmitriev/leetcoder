#include <vector>
using std::vector;

static const double EPS = 1e-6;

class Solution {
private:
  bool dfs(const vector<double> &cards) {
    if (cards.size() == 1) {
      return std::fabs(cards.back() - 24) < EPS;
    }

    const int n = cards.size();

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        vector<double> next;
        for (int k = 0; k < n; k++) {
          if (k != i && k != j) {
            next.push_back(cards[k]);
          }
        }

        vector<double> ops = {
            cards[i] + cards[j],
            cards[i] * cards[j],
            cards[i] - cards[j],
            cards[j] - cards[i],
        };

        if (cards[i] > EPS) {
          ops.push_back(cards[j] / cards[i]);
        }

        if (cards[j] > EPS) {
          ops.push_back(cards[i] / cards[j]);
        }

        for (auto op : ops) {
          next.push_back(op);
          if (dfs(next)) {
            return true;
          }
          next.pop_back();
        }
      }
    }

    return false;
  }

public:
  bool judgePoint24(vector<int> &cards) {
    vector<double> nums(cards.begin(), cards.end());
    return dfs(nums);
  }
};