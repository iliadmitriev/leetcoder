class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int left = k, right = k;
        int curMin = nums[k];
        int maxScore = nums[k];

        while (left > 0 || right < nums.size() - 1) {
            if (left == 0 || (right < nums.size() - 1 && nums[right + 1] > nums[left - 1])) {
                right++;
            } else {
                left--;
            }

            curMin = min(curMin, min(nums[left], nums[right]));
            maxScore = max(maxScore, curMin * (right - left + 1));
        }

        return maxScore;
    }
};