class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> cache;
        int res = -1;
        for (int r = 0; r < s.size(); r++) {
            if (cache.find(s[r]) != cache.end()) {
                res = max(res, r - cache[s[r]] - 1);
            } else {
                cache[s[r]] = r;
            }
        }
        return res;
    }
};