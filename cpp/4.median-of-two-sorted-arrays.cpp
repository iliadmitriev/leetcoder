class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> total;
        total.reserve(nums1.size() + nums2.size());

        total.insert(total.end(), nums1.begin(), nums1.end());
        total.insert(total.end(), nums2.begin(), nums2.end());

        std::sort(total.begin(), total.end());

        if (total.size() % 2) {
            return total[total.size() / 2];
        }
        return (total[(total.size() - 1) / 2] + total[(total.size() + 1) / 2]) / 2.0;
    }
};