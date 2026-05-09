struct pair_hash {
    template <typename T1, typename T2>
    std::size_t operator () (const std::pair<T1, T2> &p) const {
        return (p.first << 6) | (p.second) ;  
    }
};

typedef pair<int, int> Key;
typedef unordered_map<Key, int, pair_hash> Cache;


class Solution {
private:
    Cache cache{};

    int gcd(int x, int y) {
        int tmp;
        while (y) {
            tmp = y;
            y = x % y;
            x = tmp;
        }
        return x;
    }

    int dp(vector<int>& nums, int mask, int op) {
        if (op > nums.size() / 2) {
            return 0;
        }

        Key key = make_pair(mask, op);
        if (cache.find(key) != cache.end()) {
            return cache[key];
        }

        int res = 0;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if ((mask & (1 << i)) | (mask & (1 << j))) {
                    continue;
                }
                int new_mask = mask | (1 << i) | (1 << j);
                res = max(res, op * gcd(nums[i], nums[j]) + dp(nums, new_mask, op + 1));
            }
        }
        return cache[key] = res;
    }

public:
    int maxScore(vector<int>& nums) {
        cache.clear();

        return dp(nums, 0, 1);
    }
};