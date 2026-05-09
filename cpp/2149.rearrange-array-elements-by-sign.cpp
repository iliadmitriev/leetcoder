class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> pos, neg;
        int n = nums.size();
        pos.reserve(n / 2);
        neg.reserve(n / 2);

        for (auto num: nums) {
            if (num < 0) {
                neg.push_back(num);
            } else {
                pos.push_back(num);
            }
        }

        int i = 0, j = 0;

        for (int k = 0; k < n; k++) {
            if (k % 2 == 0) {
                nums[k] = pos[i++];
            } else {
                nums[k] = neg[j++];
            }
        }

        return nums;
    }
};