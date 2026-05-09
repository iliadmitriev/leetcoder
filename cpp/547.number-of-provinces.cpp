class UF {
private:
    int size;
    vector<int> parent;

public:
    UF(int _size) : size(_size), parent(vector<int>(size, 0))  {
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
        auto par_x = find(x), par_y = find(y);

        if (par_x == par_y) {
            return false;
        }
        parent[par_y] = par_x;
        return true;
    }

    int count() {
        int res = 0;
        vector<bool> vis(size, false);
        for (int v = 0; v < size; v++) {
            auto par_v = find(v);
            if (vis[par_v]) {
                continue;
            }
            vis[par_v] = true;
            res++;
        }
        return res;
    }

};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        UF uf(n);
        for (int u = 0; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                if (isConnected[u][v]) {
                    uf.join(u, v);
                }
            }
        }
        return uf.count();
    }
};