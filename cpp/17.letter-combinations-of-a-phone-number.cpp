class Solution {
private:
    std::string mp[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    std::vector<std::string> res;

    void dfs(string curr, string left) {
        if (left.empty()) {
            res.push_back(curr);
        } else {
            for (char ch : mp[left[0] - '2']) {
                dfs(curr + ch, left.substr(1));
            }
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) 
            return {};
        dfs("", digits);
        return res;
    }
};