class Solution {
public:
    bool makeEqual(vector<string>& words) {
        vector<int> counts(26, 0);
        int n = words.size();
        for (auto& word: words) {
            for (auto ch: word) {
                counts[ch - 'a']++;
            }
        }
        for (int c: counts) {
            if (c % n != 0) {
                return false;
            }
        }
        return true;
    }
};