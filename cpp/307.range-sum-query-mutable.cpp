#include <vector>

using std::vector;

class BinaryIndexTree {
private:
  vector<int> tree;

public:
  BinaryIndexTree(int n) : tree(n + 1, 0) {}

  void update(int index, int val) {
    index++;
    while (index < tree.size()) {
      tree[index] += val;
      index += index & -index;
    }
  }

  int sumRange(int index) {
    index++;
    int res = 0;
    while (index > 0) {
      res += tree[index];
      index -= index & -index;
    }
    return res;
  }
};

class NumArray {
private:
  vector<int> &_nums;
  BinaryIndexTree _tree;

public:
  NumArray(vector<int> &nums) : _nums(nums), _tree(nums.size()) {
    for (int i = 0; i < nums.size(); i++)
      _tree.update(i, nums[i]);
  }

  void update(int index, int val) {
    int delta = val - _nums[index];
    _nums[index] = val;
    _tree.update(index, delta);
  }

  int sumRange(int left, int right) {
    return _tree.sumRange(right) - _tree.sumRange(left - 1);
  }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */