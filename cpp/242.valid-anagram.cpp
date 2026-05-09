class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        int res[26] = {0};
        for (char ch: s) {
            res[ch - 'a']++;
        }

        for (char ch: t) {
            if (!res[ch - 'a']) {
                return false;
            }
            res[ch - 'a']--;
        }
        return true;
    }
};