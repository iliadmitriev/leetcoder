class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int left = 0, right = 0;
        int jumps = 0;

        while (right < n - 1) {
            int maxJump = 0;
            for (int j = left; j <= right; j++) {
                maxJump = max(maxJump, j + nums[j]);
            }
            left = right + 1;
            right = maxJump;
            jumps++;
        }

        return jumps;
    }
};