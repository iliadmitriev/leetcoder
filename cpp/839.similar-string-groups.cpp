class DSU {
private:
    vector<int> parent;
    vector<int> rank;

public:
    DSU(int size): rank(vector<int>(size, 1)), parent(vector<int>(size, 0)) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    bool join(int x, int y) {
        auto par_x = find(x);
        auto par_y = find(y);

        if (par_x == par_y) {
            return false;
        }

        if (rank[par_y] > rank[par_x]) {
            swap(par_x, par_y);
        }

        parent[par_y] = parent[par_x];
        rank[par_x] += rank[par_y];
        rank[par_y] = 0;
        return true; 
    }

    int components() {
        int res = 0;
        for (int i = 0; i < parent.size(); i++) {
            if (find(i) == i) {
                res++;
            } 
        }
        return res;
    }
};

class Solution {
private:
    bool checkSimilar(string& s1, string& s2) {
        if (s1 == s2) {
            return true;
        }
        int replacements = 0;

        for (int i = 0; i < min(s1.size(), s2.size()); i++) {
            if (s1[i] != s2[i]) {
                replacements++;
            }

            if (replacements >= 3) {
                return false;
            } 
        }
        return true;
    }

public:
    int numSimilarGroups(vector<string>& strs) {
        int n = strs.size();
        DSU dsu = DSU(n);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (checkSimilar(strs[i], strs[j])) {
                    dsu.join(i, j);
                }
            }
        }
        return dsu.components();
    }
};