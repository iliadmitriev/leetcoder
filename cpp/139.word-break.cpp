class Solution {
private:
    std::set<string> get_words(vector<string>& wordDict) {
        std::set<string> res;
        for (const auto &w : wordDict)
            res.insert(w);
        return res;
    }

    std::vector<int> get_sizes(vector<string>& wordDict) {
        std::set<int> all_sizes;
        for (const auto &w : wordDict)
            all_sizes.insert(w.size());

        std::vector<int> res;
        for (auto s : all_sizes)
            res.push_back(s);

        std::sort(res.begin(), res.end());

        return res;
    }

public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n + 1, false);
        dp[n] = true;
        std::set<string> words = get_words(wordDict);
        std::vector<int> sizes = get_sizes(wordDict);

        for (auto i = n - 1; i >= 0; i--) {
            for (auto j : sizes) {
                if (
                    i + j <= n 
                    && dp[i + j]
                    && words.count(s.substr(i, j)) != 0
                ) {
                    dp[i] = dp[i + j];
                    break;
                };  
            };
        };
        
        return dp[0];
    }
};