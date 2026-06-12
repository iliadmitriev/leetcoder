#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

/*
  Binary uplifting tree DSA
*/
class BinaryUpliftingTree {
private:
    int n;                   // number of nodes;
    int LOG;                 // max number of logarithmic jumps to root;
    vector<int> depth;       // depths on nodes
    vector<vector<int>> adj; // adjacency list adj[u] -> {v1, v2, v2, ...}
    vector<vector<int>> up; // upward ancestors of node u (logarighmic) up[u] ->
                            // [2^0, 2^1, ..., 2^j]

    // DFS algorightm for preprocessing tree
    // u - current node, p - parent node, d - current depth
    void dfs(int u, int p, int d) {
        depth[u] = d;
        up[u][0] = p;

        for (int j = 1; j < LOG; j++) {
            if (up[u][j - 1] != -1) {
                up[u][j] = up[up[u][j - 1]][j - 1];
            } else {
                up[u][j] = -1;
            }
        }

        // go to neighbourg (child nodes, skip parent)
        for (int v : adj[u]) {
            if (v == p) { // skip parent
                continue;
            }

            dfs(v, u, d + 1); // go deeper (d + 1) to child node v
        }
    }

public:
    BinaryUpliftingTree(int size)
        : n(size), LOG(std::ceil(std::log2(n)) + 1), depth(n, 0), adj(n),
          up(n, vector<int>(LOG, -1)) {};

    // add edge to graph (before preprocessing)
    void addEdge(int u, int v) {
        // TODO: without order (to be optimized later)
        if (u > v) {
          std::swap(u, v); // u < v
        }

        adj[u].push_back(v);
    }

    // preprocess before use (builds up ancestors list for nodes)
    void preprocess(int root = 0) {
        dfs(root, -1, 0); // start from root without parent (-1) with depth of 0
    }

    // find the K-th ancestor of node u
    int getKthAncestor(int u, int k) {
        for (int j = 0; j < LOG; j++) {
            if ((k >> j) & 1) { // if j-th bit of k is set
                u = up[u][j];
                if (u == -1) {
                    return -1; // above the root
                }
            }
        }

        return u;
    };

    // lowest commont ancestor of arbitrary nodes u and v
    int lca(int u, int v) {
        if (depth[u] < depth[v]) {
            std::swap(u, v);
        }

        u = getKthAncestor(u, depth[u] - depth[v]);

        if (u == v)
            return u;

        // lift both nodes simultaneously
        for (int j = LOG - 1; j >= 0; j--) {
            if (up[u][j] != up[v][j]) {
                u = up[u][j];
                v = up[v][j];
            }
        }

        // parent of u (or v) is now LCA
        return up[u][0];
    };
    // distance between arbitrary nodes u and v
    // distance[u, v] = depth[u] + depth[v] - 2 x (depth[LCA(u, v)])
    int getDistance(int u, int v) {
        int common = lca(u, v);
        return depth[u] + depth[v] - 2 * (depth[common]);
    };
};

class Solution {
private:
    const int MOD = int(1e9) + 7;
    // binary modular exponent
    int bin_mod_exp(int exp) {
        long long res = 1;
        long long base = 2;

        while (exp) {
            if (exp & 1) {
                res *= base;
                res %= MOD;
            }

            base *= base;
            base %= MOD;
            exp >>= 1;
        }

        return res;
    }

public:
    // T: O(N log N + M log N)
    // S: O(N + N log N)
    vector<int> assignEdgeWeights(vector<vector<int>>& edges,
                                  vector<vector<int>>& queries) {
        // depth[u] = number of edges upward from u to root
        // LCA(u, v) = lowest commont ancestor of both u and v
        // distance[u, v] = depth[u] + depth[v] - 2 x (depth[LCA(u, v)])
        // number of odd sum combinations of k numbers from {1,2}
        // comb(k) = (2 ^ (k - 1)) % MOD

        // in the tree (conneced graph without cycles) there is always
        // number of nodes greater then number of edges by 1
        const int n = edges.size() + 1;
        BinaryUpliftingTree bt(n); // S: O(N + N log N)

        for (vector<int>& edge : edges) {
            bt.addEdge(edge[0] - 1, edge[1] - 1); // shift 1-based to 0-based
        }

        bt.preprocess(0); // preprocess from root node; T: O(N log N)

        const int m = queries.size();
        vector<int> res(m, 0);

        // O(M log N)
        for (int i = 0; i < m; i++) {
            // shifted from 1-base to 0-based nodes u and v
            int u = queries[i][0] - 1, v = queries[i][1] - 1;

            // get distance between nodes
            int dist = bt.getDistance(u, v);
            if (dist > 0) {
                // count of number combinations from {1,2} of length k that sum
                // up to odd is a half of all combinations 2 ^ (k - 1)
                res[i] = bin_mod_exp(dist - 1);
            }
        }

        return res;
    }

    // gives TLE
    vector<int> assignEdgeWeightsTLE(vector<vector<int>>& edges,
                                     vector<vector<int>>& queries) {
        // node - 1 = edges
        const int n = edges.size() + 1;
        // build shifted to 0-base adjacency list for 1-based list of edges;
        vector<vector<int>> adj(n);
        for (vector<int>& edge : edges) {
            auto u = std::min(edge[0], edge[1]) - 1;
            auto v = std::max(edge[0], edge[1]) - 1;

            adj[u].push_back(v);
        }

        // build parent vector to iterate upward
        vector<int> parent(n, -1); // parent[child_node] = parent_node
        auto dfs = [&parent, &adj](this auto&& self, int node,
                                   int par) -> void {
            parent[node] = par;
            for (int child : adj[node]) {
                if (child == par) {
                    continue;
                }

                self(child, node);
            }
        };
        dfs(0, -1);

        // O(n), but we need O(logN)
        auto lca = [&parent](int node1, int node2) -> int {
            unordered_map<int, int> vis;
            int cnt = 0, common = node1;

            for (int n = 0; node1 != -1; n++) {
                vis[node1] = n;
                node1 = parent[node1];
            }
            for (; vis.find(node2) == vis.end(); cnt++) {
                node2 = parent[node2];
                common = node2;
            }

            return vis[common] + cnt;
        };

        vector<int> res;
        res.reserve(queries.size());

        for (vector<int>& q : queries) {
            int path = lca(q[0] - 1, q[1] - 1);
            int comb_num = path > 0 ? bin_mod_exp(path - 1) : 0;
            res.push_back(comb_num);
        }

        return res;
    }
};