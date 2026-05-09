class Solution {
public:
    int minOperations(vector<int>& nums) {
        int len = nums.size();
        std::sort(nums.begin(), nums.end());
        auto last = std::unique(nums.begin(), nums.end());
        nums.erase(last, nums.end());
        
        int window;
        int maxWindow = 0;
        int left = 0;

        for (int right = 0; right < nums.size(); right++) {
            if (nums[right] - nums[left] >= len) {
                left++;
            }
            window = right - left + 1;
            maxWindow = max(maxWindow, window);
        }
        return len - maxWindow;
    }
};