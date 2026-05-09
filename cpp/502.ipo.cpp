#include <algorithm>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>

using std::accumulate;
using std::max_element;
using std::pair;
using std::priority_queue;
using std::sort;
using std::vector;

class Solution {
public:
  int findMaximizedCapital(int k, int w, vector<int> &profits,
                           vector<int> &capital) {
    // optiomizations
    if (w >= *max_element(capital.begin(), capital.end())) {
      // aquire all projects
      if (k >= profits.size()) {
        return w + accumulate(profits.begin(), profits.end(), 0);
      }
      // aquire top k most profitable projects
      sort(profits.begin(), profits.end(), std::greater<>());
      return w + accumulate(profits.begin(), profits.begin() + k, 0);
    }

    priority_queue<int> maxProfit;

    vector<pair<int, int>> projects;
    for (int i = 0; i < profits.size(); ++i) {
      projects.push_back({capital[i], profits[i]});
    }
    sort(projects.begin(), projects.end());

    int j = 0;
    for (; k; k--) {
      while (j < projects.size() && projects[j].first <= w) {
        maxProfit.push(projects[j++].second);
      }

      if (!maxProfit.size()) {
        break;
      }

      w += maxProfit.top();
      maxProfit.pop();
    }

    return w;
  }
};