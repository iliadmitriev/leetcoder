class UnionFind {
private:
    int _components;
    vector<int> _par;
    vector<int> _rank;

public:
    UnionFind(int size): _components(size), _rank(size, 1), _par(size) {
        std::iota(_par.begin(), _par.end(), 0);
    }

    int find(int x) {
        while (x != _par[x]) {
            _par[x] = _par[_par[x]];
            x = _par[x];
        }
        return _par[x];
    }

    bool join(int x, int y) {
        int px = find(x), py = find(y);

        if (px == py) {
            return false;
        }

        if (_rank[py] > _rank[px]) {
            swap(px, py);
        }

        _rank[px] += _rank[py];
        _rank[py] = 0;
        _par[py] = _par[px];
        _components--;

        return true;
    }

    int components() {
        return _components;
    }
};

class Solution {
private:
    void factors(int num, function<void(int)> f) {
        while (num % 2 == 0) {
            f(2);
            num /= 2;
        }

        int lim = sqrt(num);
        for (int i = 3; i <= lim; i += 2) {
            while (num % i == 0) {
                f(i);
                num /= i;
            }
        }

        if (num > 2) {
            f(num);
        }
    }

public:
    bool canTraverseAllPairs(vector<int>& nums) {
        UnionFind uf(nums.size());

        map<int, int> factor_index;

        for (int i = 0; i < nums.size(); i++) {
            
            factors(nums[i], [i, &uf, &factor_index] (int num) -> void {
                if (factor_index.find(num) != factor_index.end()) {
                    uf.join(i, factor_index[num]);
                } else {
                    factor_index[num] = i;
                }
            });

        }

        return uf.components() == 1;
    }
};