#include <stack>
#include <tuple>
#include <vector>

using namespace std;
class Solution {
public:
  vector<int> sumOfDistancesInTree(int n, vector<vector<int>> &edges) {
    // sum[i] = sum[j] - count[i] + count[j]
    // count[i] = n - count[j]
    vector<vector<int>> adj(n);
    vector<int> res(n, 0);
    vector<int> count(n, 1);

    for (auto &e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    stack<tuple<int, int, bool>> st;
    st.push({0, -1, false});
    while (st.size()) {
      auto [node, prev, done] = st.top();
      st.pop();

      if (done) {
        if (prev == -1) {
          continue;
        }
        count[prev] += count[node];
        res[prev] += res[node] + count[node];
      } else {
        st.push({node, prev, true});
        for (auto child : adj[node]) {
          if (child == prev) {
            continue;
          }
          st.push({child, node, false});
        }
      }
    }

    stack<tuple<int, int>> st2;
    st2.push({0, -1});
    while (st2.size()) {
      auto [node, prev] = st2.top();
      st2.pop();

      for (auto child : adj[node]) {
        if (child == prev) {
          continue;
        }
        res[child] = res[node] + n - count[child] - count[child];
        st2.push({child, node});
      }
    }

    return res;
  }
};