class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        const int total = std::reduce(nums.begin(), nums.end());
        const int n = nums.size();
        int f = 0;

        // calculate base f(0)
        for (int i = 0; i < n; i++) {
            f += i * nums[i];
        }

        int res = f; // set base result as f(0)

        /*
        f(0) = 0 * num0 + 1 * num1 + ... + n-1 * num_n-1
        f(1) = 1 * num0 + 2 * num1 + ... +   0 * num_n-1
        f(1) - f(0) = num0 + num1 + ... + -n-1 * num_n-1 = sum - n-1 * num_n-1
        f(1) = f(0) + sum - num_n-1
        */

        for (int i = 0; i < n; i++) {
            f += +total - n * nums[n - i - 1];
            res = std::max(res, f);
        }

        return res;
    }
};