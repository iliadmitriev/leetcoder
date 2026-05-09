class Solution {
private:
    bool dp(int p1, int p2, int i, int j, vector<int>& nums) {
        if (i > j) return p1 >= p2;
        if (i == j) return p1 + nums[i] >= p2;

        return (dp(p1 + nums[i], p2 + nums[j], i + 1, j - 1, nums) 
                && dp(p1 + nums[i], p2 + nums[i + 1], i + 2, j, nums)) ||
                (dp(p1 + nums[j], p2 + nums[i], i + 1, j - 1, nums) 
                && dp(p1 + nums[j], p2 + nums[j - 1], i, j - 2, nums));
    }
public:
    bool PredictTheWinner(vector<int>& nums) {
        
        return dp(0, 0, 0, nums.size() - 1, nums);
    }
};