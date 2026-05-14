class Solution {
public:
    bool isGood(vector<int>& nums) {
        const int n = nums.size();
        vector<int> cnt(n, 0);

        for (int num : nums) {
            if (num >= n || num < 1) {
                return false;
            }
            if (num < n - 1 && cnt[num] > 0) { // <(n-1) no repeat
                return false;
            }
            if (num == n - 1 && cnt[num] > 1) { // (n-1) repeat once
                return false;
            }

            cnt[num]++;
        }

        return true;
    }
};