class Solution {
public:
    int minOperations(vector<int>& nums) {
        const int n = nums.size();
        if (n <= 1) {
            return 0;
        }

        // get zero position;
        int zero = std::distance(nums.begin(), std::find(nums.begin(), nums.end(), 0));

        bool asc = true, desc = true;

        for (int i = 1; i < n; i++) {
            int j = (i + zero) % n;

            if (nums[j] != i) {
                asc = false;
            }
            
            if (nums[j] != n - i) {
                desc = false;
            }

            if (!asc && !desc) {
                return -1;
            }
        }

        if (asc) {
            return std::min(zero, n - zero + 2);
        }

        return std::min(n - zero, zero + 2);
    }
};