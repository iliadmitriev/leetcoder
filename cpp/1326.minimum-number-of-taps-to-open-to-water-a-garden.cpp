class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> maxRanges(n + 1, 0);

        for (int i = 0; i < n + 1; i++) {
            int start = max(0, i - ranges[i]);
            int end = min(n, i + ranges[i]);
            maxRanges[start] = max(maxRanges[start], end);
        }

        int taps = 0;
        int maxEnd = 0;
        int curEnd = 0;

        for (int j = 0; j <= n; j++) {
            if (maxEnd < j){
                return -1;
            }

            if (curEnd < j) {
                curEnd = maxEnd;
                taps++;
            }

            if (maxEnd < maxRanges[j]) {
                maxEnd = maxRanges[j];
            }
        }

        return taps;
    }
};