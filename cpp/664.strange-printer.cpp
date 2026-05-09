class Solution {
private:
    int size;
    std::vector<vector<int>> cache;
    std::string str;

    int dp(int left, int right) {
        if (left >= right) return 0;
        if (cache[left][right] != -1) return cache[left][right];

        int res = size;

        auto j = -1;

        for (auto i = left; i < right; i++) {
            if (str[i] != str[right] && j == -1)
                j = i;
            if (j != -1)
                res = min(
                    res,
                    1 + dp(j, i) + dp(i + 1, right)
                );
        };

        if (j == -1)
            res = 0;

        cache[left][right] = res;
        return res;
    }

public:
    int strangePrinter(string s) {

        for (auto i = 0; i < s.size(); i++)
            if (i == 0 || s[i] != s[i - 1]) 
                str.push_back(s[i]);

        size = str.size();
        cache = std::vector<vector<int>>(size, std::vector<int>(size, -1));

        return dp(0, size - 1) + 1;
        
    }
};