#include <functional>
#include <queue>
#include <unordered_map>
#include <vector>

using std::unordered_map, std::priority_queue, std::greater, std::vector;

class NumberContainers {
public:
  NumberContainers() {}

  void change(int index, int number) {
    nums[index] = number;
    idx[number].push(index);
  }

  int find(int number) {
    if (!idx.count(number) || idx[number].empty()) {
      return -1;
    }

    while (!idx[number].empty()) {
      if (nums[idx[number].top()] == number) {
        return idx[number].top();
      } else {
        idx[number].pop();
      }
    }

    return -1;
  }

private:
  typedef priority_queue<int, vector<int>, greater<int>> MinHeap;

  unordered_map<int, int> nums;    // index -> number
  unordered_map<int, MinHeap> idx; // number -> min index heap
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */