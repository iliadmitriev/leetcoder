class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int canJumpUpTo = 0;
        
        for (int j = 0; j <= canJumpUpTo; j++) {
            
            if (j == n - 1)
                return true;

            if (j + nums[j] > canJumpUpTo) {
                canJumpUpTo = j + nums[j];
            }
        }

        return false;
    }
};