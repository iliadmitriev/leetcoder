class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res = 0, count = 0;

        for (const auto& num: nums) {
            if (count == 0) {
                res = num;
            }
            if (res == num) {
                count++;
            } else {
                count--;
            }
        }
        return res;
    }
};