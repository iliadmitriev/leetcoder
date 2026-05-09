class UnionFind {
private:
    vector<int> parent;
    vector<int> rank;
public:
    UnionFind(int size) : rank(size, 1), parent(size) {
        std::iota(std::begin(parent), std::end(parent), 0);
    }

    void reset() {
        std::fill(rank.begin(), rank.end(), 1);
        std::iota(std::begin(parent), std::end(parent), 0);
    }

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    bool join(int v1, int v2) {
        int p1 = find(v1), p2 = find(v2);

        if (p1 == p2)
            return false;

        if (rank[p1] > rank[p2])
            swap(p1, p2);

        parent[p1] = p2;
        rank[p2] += rank[p1];
        rank[p1] = 0;

        return true;
    }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        typedef tuple<int, int, int, int> edge;
        vector<edge> sorted_edges;

        for (int i = 0; i < edges.size(); i++)
            sorted_edges.push_back(make_tuple(edges[i][0], edges[i][1], edges[i][2], i));

        std::sort(sorted_edges.begin(), sorted_edges.end(), [](const edge& a, const edge& b)
        { 
            return get<2>(a) < get<2>(b); 
        });

        vector<int> critical, pseudo;
        UnionFind uf_base = UnionFind(n);
        UnionFind uf_curr = UnionFind(n);

        for (const auto [u1, v1, w1, i] : sorted_edges) {
            uf_base.reset(); uf_curr.reset();

            int weight_base = 0, weight_curr = 0;
            // force current base edge to be a part of candidate MST
            uf_base.join(u1, v1);
            weight_base += w1;

            for (const auto [u2, v2, w2, j] : sorted_edges) {
                if (i == j)
                    continue;

                if (uf_base.join(u2, v2))
                    weight_base += w2;
                
                if (uf_curr.join(u2, v2))
                    weight_curr += w2;
            };

            // if total weight of current MST is greater or graph is disconnected
            // (unable to create MST without i-th edge)
            // then candidate i-th edge is critical
            if (weight_curr > weight_base || uf_curr.join(v1, u1))
                critical.push_back(i);
            else if (weight_curr == weight_base)
                // if we are able to build MST with the same weight
                // then candidate i-th edge is pseudo-critical
                pseudo.push_back(i);
        };

        return {critical, pseudo};
        
    }
};