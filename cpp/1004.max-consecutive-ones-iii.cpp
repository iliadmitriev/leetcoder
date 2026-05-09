class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int i = 0, j = 0;

        for (; j < n; j++) {
            if (nums[j] == 0) {
                k--;
            }

            if (k < 0) {
                if (nums[i] == 0) {
                    k++;
                }
                i++;
            }
        }

        return j - i;
    }
};