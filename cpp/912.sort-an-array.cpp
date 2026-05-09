#include <vector>

using std::vector;

class Solution {
private:
  void heapify(vector<int> &arr, int start, int end) {
    int parent = start, child = 2 * start + 1;

    while (child <= end) {
      if (child < end && arr[child] < arr[child + 1])
        child++;

      if (arr[parent] < arr[child]) {
        std::swap(arr[parent], arr[child]);
        parent = child;
        child = 2 * parent + 1;
      } else {
        break;
      }
    }
  }

  void heapSort(vector<int> &arr) {
    int n = arr.size();

    for (int i = n - 1; i >= 0; i--) {
      heapify(arr, i, n - 1);
    }

    for (int i = n - 1; i > 0; i--) {
      std::swap(arr[0], arr[i]);
      heapify(arr, 0, i - 1);
    }
  }

public:
  vector<int> sortArray(vector<int> &nums) {
    heapSort(nums);
    return nums;
  }
};