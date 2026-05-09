class Solution {
private:
    int binSearch(vector<int>& arr, int target) {
        int lo = 0; int hi = arr.size();
        int mid;

        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size(); int n = text2.size();
        
        map<char, vector<int>> t2;
        for (int i = 0; i < n; i++) {
            t2[text2[i]].push_back(i);
        }

        vector<int> dp;

        for (char ch: text1) {
            if (t2.find(ch) == t2.end()) {
                continue;
            }

            for (auto it = t2[ch].rbegin(); it != t2[ch].rend(); it++) {
                int i = binSearch(dp, *it);

                if (i == dp.size()) {
                    dp.push_back(*it);
                } else {
                    dp[i] = *it;
                }
            }
        }

        return dp.size();
    }
};