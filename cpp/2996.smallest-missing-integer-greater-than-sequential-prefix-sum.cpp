class Solution {
public:
    int missingInteger(vector<int>& nums) {
       const int n = nums.size();
        unordered_set<int> uniq(nums.begin(), nums.end());

        int pre = nums.front();
        int i = 1;

        while (i < n && nums[i - 1] + 1 == nums[i]) {
            pre += nums[i++];
        }

        while (uniq.count(pre)) {
            pre++;
        }

        return pre;
    }
};