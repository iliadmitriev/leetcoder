class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0);

        int total = 0, i = 0, j = 0;

        while (i < neededTime.size()) {
            int curTime = 0, curMax = neededTime[i];

            while (j < neededTime.size() && colors[i] == colors[j]) {
                curTime += neededTime[j];
                curMax = max(curMax, neededTime[j]);
                j++;
            }

            total += curTime - curMax;
            i = j;
        }
        return total;
    }
};