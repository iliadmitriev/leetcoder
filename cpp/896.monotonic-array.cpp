class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool le = true, ge = true;

        for (size_t i = 0; i < nums.size() - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                le = false;
            }

            if (nums[i] > nums[i + 1]) {
                ge = false;
            }

            if (!ge && !le) {
                break;
            }
        }

        return le || ge;
    }
};