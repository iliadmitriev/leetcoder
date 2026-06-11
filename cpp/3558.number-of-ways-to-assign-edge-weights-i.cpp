#include <vector>
#include <unordered_map>

using std::vector, std::unordered_map;

class Solution {
public:
    int assignEdgeWeights(vector<vector<int>>& edges) {
      const int MOD = int(1e9) + 7;

      const int n = edges.size() + 2;
      // 3 edges: 2 childs + 1 parent
      vector<vector<int>> adj(n); 

      for (vector<int>& edge : edges ) {
        adj[edge[0]].push_back(edge[1]);
        adj[edge[1]].push_back(edge[0]);
      }

      auto dfs = [&adj](this auto&& self, int node, int parent) -> int {
        int d = 0;

        for (int child : adj[node]) {
          if (child == parent || child == 0) {
            continue;
          }

          d = std::max(d, 1 + self(child, node));
        }

        return d;
      };

      auto mod_pow = [](long long n, long long m) -> long long {
        long long result = 1;
        long long base = 2 % m;

        while (n > 0) {
          if (n & 1) {
            result = (result * base) % m;
          }

          base = (base * base) % m;
          n >>= 1;
        }

        return result;
      };

      int k = dfs(1, -1);

      return mod_pow(k - 1, MOD);
    }
};