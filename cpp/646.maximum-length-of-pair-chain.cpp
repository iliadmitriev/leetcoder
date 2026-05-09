class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {

        sort(pairs.begin(), pairs.end(), [&](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int length = 1;
        int end = pairs[0][1];

        for (int i = 0; i < pairs.size(); i++) {
            if (end < pairs[i][0]) {
                end = pairs[i][1];
                length++;
            }
        }
        return length;
    }
};