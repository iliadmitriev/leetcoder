class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        const int n = nums.size();
        int cnt = 0, res = 0;

        for (int l = 0; l < n; l++) {

            // Boyer-Moore majority voating
            cnt = 0;

            for (int r = l; r < n; r++) {
                cnt += nums[r] == target ? 1 : -1;

                if (cnt > 0) {
                    res++;
                }
            }
        }

        return res;
    }
};