class Solution {
public:
    int minSteps(string s, string t) {
        int cache[26] = {0};

        for (char ch: s) {
            cache[ch - 'a']++;
        }

        for (char ch: t) {
            cache[ch - 'a']--;
        }

        int res = 0;
        for (auto c: cache) {
            res += c > 0 ? c : 0;
        }

        return res;
    }
};