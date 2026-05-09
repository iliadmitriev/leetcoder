class Solution {
private:
    bool dp(int i, int k, int last, set<int>& stone_set, map<pair<int, int>, bool>& cache) {
        
        // speed can't be 0
        if (k == 0) return false;

        // if reached final last stone
        if (i == last) return true;

        // check if current step is not possible
        if (stone_set.find(i + k) == stone_set.end())
            return false;

        // if found previous calculations
        if (cache.count( make_pair(i, k) ) == 1)
            return cache[make_pair(i, k)];

        // try to find positive result with k - 1, k and k + 1 step
        bool res = false;
        for (int step : {-1, 0, 1}) {
            if ( dp(i + k, k + step, last, stone_set, cache) ) {
                res = true;
                break;
            }
        }

        // cache and return result
        return cache[make_pair(i, k)] = res;
    }

public:
    bool canCross(vector<int>& stones) {
        set<int> stone_set(stones.begin(), stones.end());
        map<pair<int, int>, bool> cache;
        int last = stones[stones.size() - 1];

        return dp(0, 1, last, stone_set, cache);
    }
};