class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int max1 = std::numeric_limits<int>::min(); int max2 = std::numeric_limits<int>::min();
        int min1 = std::numeric_limits<int>::max(); int min2 = std::numeric_limits<int>::max();

        for (int n: nums) {
            if (max1 < n) {
                max2 = max1; max1 = n;
            } else if (max2 < n) {
                max2 = n;
            }

            if (min1 > n) {
                min2 = min1; min1 = n;
            } else if (min2 > n) {
                min2 = n;
            }
        }

        return (max1 * max2) - (min1 * min2);
    }
};