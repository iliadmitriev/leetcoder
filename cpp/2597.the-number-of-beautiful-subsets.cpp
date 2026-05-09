class Solution {
private:
  int subsetCount(const vector<int> &nums, vector<int> &subset, int i, int k) {
    if (i >= nums.size()) {
      return subset.size() > 0 ? 1 : 0;
    }

    int res = 0;
    if (nums[i] - k < 0 ||
        !std::binary_search(subset.begin(), subset.end(), nums[i] - k)) {
      subset.push_back(nums[i]);
      res += subsetCount(nums, subset, i + 1, k);
      subset.pop_back();
    }

    res += subsetCount(nums, subset, i + 1, k);
    return res;
  }

public:
  int beautifulSubsets(vector<int> &nums, int k) {
    sort(nums.begin(), nums.end());
    vector<int> subset;
    return subsetCount(nums, subset, 0, k);
  }
};