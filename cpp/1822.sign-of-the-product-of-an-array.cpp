class Solution {
public:
    int arraySign(vector<int>& nums) {
        int product = std::accumulate(nums.begin(), nums.end(), 1, [&](int a, int b) {
            return (a > 0 &&  b > 0) || (a < 0 && b < 0) ? 1 : a == 0 || b == 0 ? 0 : -1 ;
        });
        return (product > 0) - (product < 0);
    }
};