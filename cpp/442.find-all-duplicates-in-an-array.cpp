class Solution {
public:
  vector<int> findDuplicates(vector<int> &nums) {
    // use position in nums to mark nums[i] - 1 as negative
    // if number is negative, then it is duplicate
    vector<int> res;
    for (auto &num : nums) {
      if (nums[abs(num) - 1] < 0) {
        res.push_back(abs(num));
      } else {
        nums[abs(num) - 1] *= -1;
      }
    }

    return res;
  }
};