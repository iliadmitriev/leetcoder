class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {

        unordered_set<int> s1(nums1.begin(), nums1.end());
        unordered_set<int> s2(nums2.begin(), nums2.end());

        unordered_set<int> res1;
        unordered_set<int> res2;

        for (auto el : s1) {
            if (s2.find(el) == s2.end()) {
                res1.insert(el);
            }
        }

        for (auto el : s2) {
            if (s1.find(el) == s1.end()) {
                res2.insert(el);
            }
        }

        return vector<vector<int>>({
            vector<int>(res1.begin(), res1.end()),
            vector<int>(res2.begin(), res2.end())
        });
    }
};