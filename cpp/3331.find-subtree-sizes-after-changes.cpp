#include <array>
#include <ranges>
#include <string>
#include <string_view>
#include <vector>

using std::vector, std::string;

class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        const int n = parent.size();
        vector<vector<int>> adj(n);

        for (int v : std::views::iota(1, n)) {
            adj[parent[v]].push_back(v);
        }

        std::vector<int> sizes(n, 1); // the node itself as a base value

        std::array<int, 26> last;
        last.fill(-1);

        auto dfs = [&](this auto&& self, int v) -> void {
            const int label = s[v] - 'a';
            const int anc = last[label]; // preserve the ancestor for a label

            last[label] = v; // set the ancestor for the descendant nodes

            for (int u : adj[v]) {
                self(u); // dfs for child nodes
            }

            last[label] = anc; // revert the ancestor for the label

            // drop the root (no parent)
            if (v <= 0) {
                return;
            }

            // append result to the ancestor of the same label or the parent
            const int p = (anc >= 0) ? anc : parent[v];
            sizes[p] += sizes[v];
        };

        dfs(0);

        return sizes;
    }
};