class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        int f = 0, f1 = 0, f2 = 0, f3 = 0;

        for (int cost : costs) {
            f = cost + std::min(f1 + 1, std::min(f2 + 4, f3 + 9));

            f3 = f2;
            f2 = f1;
            f1 = f;
        }

        return f;
    }
};