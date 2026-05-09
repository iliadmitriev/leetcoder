class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        long total = 0, res = -1;

        for (auto num: nums) {
            if (total > num) {
                res = total + num;
            }

            total += num;
        }

        return res;
    }
};