class Solution {
private:
  unordered_map<int, int> getMap(vector<int> &arr) {
    unordered_map<int, int> mp;
    for (int i = 0; i < arr.size(); ++i) {
      ++mp[arr[i]];
    }
    return mp;
  }

public:
  bool canBeEqual(vector<int> &target, vector<int> &arr) {
    return getMap(target) == getMap(arr);
  }
};