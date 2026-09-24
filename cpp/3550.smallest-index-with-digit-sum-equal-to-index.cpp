class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        auto digits = [](int x) -> int {
            int y = 0;
            while (x) {
                y += x % 10;
                x /= 10;
            }
            return y;
        };

        for (int i = 0; i < nums.size(); i++) {
            if (i == digits(nums[i])) {
                return i;
            }
        }

        return -1;
    }
};