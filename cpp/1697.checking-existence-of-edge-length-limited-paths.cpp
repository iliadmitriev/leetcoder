class DSU {
private:
    int size;
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int _size): size(_size), rank(_size, 1), parent(_size, 0) {
        std::iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    bool join(int x, int y) {
        int par_x = find(x);
        int par_y = find(y);

        if (par_x == par_y) {
            return false;
        }

        if (rank[par_y] > rank[par_x]) {
            swap(par_y, par_x);
        }

        parent[par_y] = par_x;
        rank[par_x] += rank[par_y];
        rank[par_y] = 0;
        return true;
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

class Solution {
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList, vector<vector<int>>& queries) {
        DSU dsu = DSU(n);
        // sort (u, v, distance) by distance ascending
        std::sort(edgeList.begin(), edgeList.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] < b[2];
        });
        // add indexes to queries and sort (from, to, limit, index) by limit ascending
        int i = 0;
        std::for_each(queries.begin(), queries.end(), [&](vector<int>& item) {
            item.push_back(i++);
        });
        std::sort(queries.begin(), queries.end(), [](vector<int>& a, vector<int>& b) {
            return a[2] < b[2];
        });


        int edgeIdx = 0;
        vector<bool> res(queries.size(), false);
        for (int i = 0; i < queries.size(); i++) {
            while (edgeIdx < edgeList.size() && edgeList[edgeIdx][2] < queries[i][2]) {
                dsu.join(edgeList[edgeIdx][0], edgeList[edgeIdx][1]);
                edgeIdx++;
            }

            res[queries[i][3]] = dsu.connected(queries[i][0], queries[i][1]);
        }

        return res;
    }
};