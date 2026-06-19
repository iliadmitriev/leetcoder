class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int runningTotal = 0;
        int runningMax = 0;

        for (int g : gain) {
            runningTotal += g;
            runningMax = std::max(runningMax, runningTotal);
        }

        return runningMax;
    }
};