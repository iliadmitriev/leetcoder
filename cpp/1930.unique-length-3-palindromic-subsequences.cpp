class Solution {
private:
    int countUnique(string& s, int i, int j) {
        set<char> d;
        for (; i < j; i++) {
            d.insert(s[i]);
            // optimization: alphabet size is bounded to 26
            if (d.size() == 26) {
                return 26;
            }
        }
        return d.size();
    }
public:
    int countPalindromicSubsequence(string s) {
        map<char, vector<int>> m;
        for (int i = 0; i < s.size(); i++) {
            m[s[i]].push_back(i);
        }

        int res = 0;
        for (auto [k, v] : m) {
            if (v.size() < 2) {
                continue;
            }

            int left = *(v.begin()) + 1; // left pointer shifted right 
            int right = *(v.end() - 1); // right pointer is shifled already

            res += countUnique(s, left, right);

        }
        return res;
    }
};