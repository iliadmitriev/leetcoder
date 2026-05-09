class Solution {
public:
  vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
    unordered_set<int> set;
    vector<int> res;

    for (auto num : nums1) {
      set.insert(num);
    }

    for (auto num : nums2) {
      if (set.find(num) != set.end()) {
        res.push_back(num);
        set.erase(num);
      }
    }

    return res;
  }
};