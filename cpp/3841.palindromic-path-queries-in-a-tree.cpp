#include <sstream>
#include <string>
#include <vector>

using std::vector, std::string;

class BinaryIndexTree {
private:
    int n;
    vector<int> tree;

    inline int lowbit(int i) { return i & -i; }

public:
    BinaryIndexTree(int _n) : tree(_n + 1, 0), n{_n} {}

    void update(int i, int v) {
        while (i <= n) {
            tree[i] ^= v;
            i += lowbit(i);
        }
    }

    int query(int i) {
        int res = 0;
        while (i > 0) {
            res ^= tree[i];
            i -= lowbit(i);
        }

        return res;
    }

    void update_range(int l, int r, int v) {
        update(l, v);
        update(r + 1, v);
    }
};

class BinaryUpliftTree {
private:
    int LOG;
    int n, t;
    vector<int> l, r, dep;
    vector<vector<int>> fa;

    void _dfs(const vector<vector<int>>& g, int u, int p) {
        t++;
        l[u] = t;
        fa[u][0] = p;

        for (int v : g[u]) {
            if (v == p) {
                continue;
            }

            dep[v] = dep[u] + 1;

            _dfs(g, v, u);
        }

        r[u] = t;
    }

public:
    BinaryUpliftTree(int _n) : n{_n}, t{0}, l(_n, 0), r(_n, 0), dep(_n, 0) {
        LOG = std::bit_width(static_cast<unsigned int>(_n));
        fa = vector<vector<int>>(n, vector<int>(LOG, 0));
    }

    void build(const vector<vector<int>>& g) {
        _dfs(g, 0, 0);

        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                fa[i][j] = fa[fa[i][j - 1]][j - 1];
            }
        }
    }

    int lca(int u, int v) {
        if (dep[u] < dep[v]) {
            std::swap(u, v);
        }

        int diff = dep[u] - dep[v];
        for (int i = 0; i < LOG; i++) {
            if ((diff >> i) & 1) {
                u = fa[u][i];
            }
        }

        if (u == v) {
            return u;
        }

        for (int i = LOG - 1; i >= 0; i--) {
            if (fa[u][i] != fa[v][i]) {
                u = fa[u][i];
                v = fa[v][i];
            }
        }

        return fa[u][0];
    }

    inline int left(int i) { return l[i]; }

    inline int right(int i) { return r[i]; }
};

class Solution {
private:
    inline int char_bit(char ch) { return 1 << (ch - 'a'); }

public:
    vector<bool> palindromePath(int n, vector<vector<int>>& edges, string s,
                                vector<string>& queries) {
        vector<vector<int>> g(n, vector<int>());
        for (const auto& edge : edges) {
            g[edge[0]].push_back(edge[1]);
            g[edge[1]].push_back(edge[0]);
        }

        vector<bool> res;
        res.reserve(queries.size());

        BinaryIndexTree bit(n + 1);

        BinaryUpliftTree but(n);
        but.build(g);

        for (int i = 0; i < n; i++) {
            bit.update_range(but.left(i), but.right(i), char_bit(s[i]));
        }

        for (const auto& q : queries) {
            std::stringstream ss(q);
            string op;
            ss >> op;

            if (op == "update") {
                int u;
                char ch;
                ss >> u >> ch;

                bit.update_range(but.left(u), but.right(u),
                                 char_bit(ch) ^ char_bit(s[u]));
                s[u] = ch;
            } else {
                int u, v;
                ss >> u >> v;
                int w = but.lca(u, v);
                int mask = bit.query(but.left(u)) ^ bit.query(but.left(v)) ^
                           char_bit(s[w]);
                res.push_back((mask & (mask - 1)) == 0);
            }
        }

        return res;
    }
};