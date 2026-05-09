class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        int n = s.length();
        vector<int> dp(n + 1, n + 1);
        dp[n] = 0; // base case

        // optimization 1: unique set of words with O(1) access time
        // optimization 2: unique set of lengths instead of iterating all lengths from 0 .. n
        set<int> lengths;
        set<string> vocab;
        for (string& word : dictionary) {
            vocab.insert(word);
            lengths.insert(word.length());
        }

        for (int pos = n - 1; pos >= 0; pos--) {
            for (int len : lengths) {
                if (pos + len <= n && vocab.find(s.substr(pos, len)) != vocab.end()) {
                    dp[pos] = min(dp[pos], dp[pos + len]);
                }
            }
            dp[pos] = min(dp[pos], 1 + dp[pos + 1]);
        }

        return dp[0];
    }
};