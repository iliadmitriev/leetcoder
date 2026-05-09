class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        // cost to get to k-2 index and k-1
        // (two previous values before k)
        int k_2 = 0; int k_1 = 0;
        int k = 0;

        for (int i = 2; i <= cost.size(); i++) {
            k = min(k_2 + cost[i - 2], k_1 + cost[i - 1]);
            k_2 = k_1;
            k_1 = k;
        }
        return k;
    }
};