class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        if (g.size() == 0 || s.size() == 0)
            return 0;

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int i = 0;
        int n = g.size(); int m = s.size();

        for (int j = 0; j < m && i < n; j++) {
            if (g[i] <= s[j]) {
                i++;
            }
        }
        return i;
    }
};