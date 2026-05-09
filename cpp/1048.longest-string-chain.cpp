class Solution {
public:
    int longestStrChain(vector<string>& words) {
        unordered_map<string, int> cache; // word -> current max length
        map<int, vector<string>> len; // length -> list of words
        int res = 0;

        // build map word length -> list of words
        for (const auto& word: words) {
            len[word.size()].push_back(word);
        }

        for (int l = 1; l < 17; l++) {
            for (const auto& word : len[l]) {
                int maxLen = 0;
                for (int j = 0; j < l; j++) {
                    string key(word.substr(0, j) + word.substr(j + 1));
                    maxLen = max(maxLen, cache[key]);
                }
                cache[word] = 1 + maxLen;
                res = max(res, cache[word]);
            }
        }
        return res;
    }
};