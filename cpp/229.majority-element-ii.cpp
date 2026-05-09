class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int cnt1 = 0, cnt2 = 0;
        int el1 = std::numeric_limits<int>::min();
        int el2 = std::numeric_limits<int>::min();

        for (const auto& num : nums) {
            if (cnt1 == 0 && num != el2) {
                el1 = num;
                cnt1 = 1;
            } else if (cnt2 == 0 && num != el1) {
                el2 = num;
                cnt2 = 1;
            } else if (num == el1) {
                cnt1++;
            } else if (num == el2) {
                cnt2++;
            } else {
                cnt1--;
                cnt2--;
            }
        }
        vector<int> res;
        if (std::count(nums.begin(), nums.end(), el1) > nums.size() / 3) {
            res.push_back(el1);
        }
        if (std::count(nums.begin(), nums.end(), el2) > nums.size() / 3) {
            res.push_back(el2);
        }
        return res;
    }
};