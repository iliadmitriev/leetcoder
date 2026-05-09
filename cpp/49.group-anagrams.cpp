class Solution {
private:
    string anag(string& s) {
        string temp(s);
        std::sort(temp.begin(), temp.end());
        return temp;
    }
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> mp;

        for (auto& word : strs) {
            mp[anag(word)].push_back(word);
        }

        for (auto& [k, v]: mp) {
            res.push_back(v);
        }
        return res;
    }
};