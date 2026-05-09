#include <queue>
#include <vector>
using std::vector, std::priority_queue;

class Solution {
private:
  inline int divide(int x, int y) { return x % y ? x / y + 1 : x / y; }

public:
  long long maxKelements(vector<int> &nums, int k) {
    priority_queue<int> maxHeap(nums.begin(), nums.end());
    long long score = 0;

    while (k) {
      int top = maxHeap.top();
      maxHeap.pop();

      if (top == 1) {
        score += k;
        k = 0;
      } else {
        score += top;
        maxHeap.push(divide(top, 3));
        k--;
      }
    }

    return score;
  }
};