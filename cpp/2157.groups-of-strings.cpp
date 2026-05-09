class DSU {
private:
    size_t _size;
    vector<int> parent;
    vector<int> rank;

public:
    DSU(size_t size): _size(size), parent(size, 0), rank(size, 1) {
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
            swap(par_x, par_y);
        }

        parent[par_y] = par_x;
        rank[par_x] += rank[par_y];
        rank[par_y] = 0;
        return true;
    }

    vector<int> getComponents() {
        int count = 0;
        unordered_map<int, int> maxComponentSize;

        for (int i; i < _size; i++) {
            auto key = find(i);
            count += key == i;
            maxComponentSize[key]++;
        }
        int maxSize = 0;
        for (const auto& [_, value] : maxComponentSize) {
            maxSize = max(maxSize, value);
        }

        return {count, maxSize};
    }
};

class Solution {
private:
    int getMask(const string& word) {
        int res = 0;
        for (char ch : word) {
           res |= 1 << (ch - 'a');
        }
        return res;
    }

public:
    vector<int> groupStrings(vector<string>& words) {
        size_t n = words.size();
        DSU dsu = DSU(n);
        unordered_map<int, int> cache; // map: mask -> index

        for (int i = 0; i < n; i++) {
            auto mask = getMask(words[i]);
            
            // if we have current word index already in cache,
            // then it's duplicate, join this words
            if (cache.find(mask) != cache.end()) {
                dsu.join(i, cache[mask]);
            } else {
                // otherwise add index to cache
                cache[mask] = i;
            }

            // iterate bits of mask
            for (int j = 0; j < 26; j++) {
                // if current bit is 1
                if (mask & (1 << j)) {
                    // turn this bit off
                    auto key = mask ^ (1 << j);

                    // if this mask is found
                    if (cache.find(key) != cache.end()) {
                        // join index of mask wiht current index
                        dsu.join(i, cache[key]);
                    } else {
                        // otherwise add to cache
                        cache[key] = i;
                    }

                }
            }
        }

        return dsu.getComponents();
    }
};