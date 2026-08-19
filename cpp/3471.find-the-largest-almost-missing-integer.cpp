class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        const int n = nums.size();
        // if obly one subarray
        if (n == k) {
            return std::ranges::max(nums);
        }

        std::unordered_map<int, int> c;
        for (int x : nums) {
            c[x]++;
        }

        // if each element is subarray

        if (k == 1) {
            int mm = -1;
            for (int x : nums) {
                if (c[x] == 1) {
                    mm = std::max(mm, x);
                }
            }
            return mm;
        }

        int c1 = nums.front(), c2 = nums.back();
        c1 = c[c1] == 1 ? c1 : -1;
        c2 = c[c2] == 1 ? c2 : -1;

        return std::max(c1, c2);
    }
};