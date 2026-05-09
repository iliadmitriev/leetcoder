#include <iostream>
#include <ostream>
#include <vector>

using std::vector;

class ProductOfNumbers {
private:
  vector<int> nums;

public:
  ProductOfNumbers() : nums({1}) {}

  void add(int num) {
    if (num == 0) {
      nums.clear();
      nums.push_back(1);
      return;
    }

    nums.push_back(nums.back() * num);
  }

  int getProduct(int k) {

    if (k >= nums.size()) {
      return 0;
    }

    return nums.back() / nums[nums.size() - k - 1];
  }
};
