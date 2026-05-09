class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int p[26]{};
        for (auto ch: chars) { p[ch - 'a']++; }

        int res = 0; int add;
        for (const string& word: words) {
            
            add = word.size();

            if (add > chars.size()) {
                continue;
            }
            
            int w[32]{};
            for (char ch: word) { w[ch - 'a']++; }

            for (int i = 0; i < 26; i++) {
                if (w[i] > p[i]) {
                    add = 0;
                    break;
                }
            }

            res += add;

        }

        return res;
    }
};