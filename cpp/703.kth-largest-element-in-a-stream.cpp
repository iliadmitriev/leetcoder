#include <queue>
#include <vector>

using std::priority_queue;
using std::vector;

class KthLargest {
private:
  int pos;
  priority_queue<int, vector<int>, std::greater<int>> data;

public:
  KthLargest(int k, vector<int> &nums) : data(nums.begin(), nums.end()) {
    pos = k;
    while (data.size() > k) {
      data.pop();
    }
  }

  int add(int val) {
    data.push(val);
    while (data.size() > pos) {
      data.pop();
    }

    return data.top();
  }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */