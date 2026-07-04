#include <limits>
#include <vector>

using std::vector;

class UF {
private:
    int cap;
    vector<int> par;
    vector<int> min;

public:
    UF(int cap) : cap(cap), par(cap), min(cap) {
        const int inf = std::numeric_limits<int>::max();

        std::iota(par.begin(), par.end(), 0);
        std::fill(min.begin(), min.end(), inf);
    }

    int find(int x) {
        while (x != par[x]) {
            par[x] = par[par[x]];
            x = par[x];
        }

        return x;
    }

    void join(int x, int y, int w) {
        int parX = find(x), parY = find(y);

        int cur = std::min(min[parX], min[parY]);
        par[parY] = parX;
        min[parX] = std::min(cur, w);
    }

    int getMin(int x) { return min[find(x)]; }
};

class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        UF uf = UF(n);

        for (vector<int>& v : roads) {
            uf.join(v[0] - 1, v[1] - 1, v[2]);
        }

        return uf.getMin(n - 1);
    }
};