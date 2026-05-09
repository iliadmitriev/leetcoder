#include <iostream>
#include <string>
#include <vector>

using std::string, std::vector;

static int zero = []() {
  std::cin.tie(nullptr);
  std::ios::sync_with_stdio(false);
  return 0;
}();

class Solution {
public:
  vector<int> minOperations(string boxes) {
    const int N = boxes.size();
    int leftCnt = 0, rightCnt = 0;
    int leftSum = 0, rightSum = 0;

    for (int i = 0; i < N; i++) {
      int box = boxes[i] == '1';
      rightCnt += box;
      rightSum += box * (i + 1); // abs diff between -1 and i
    }

    vector<int> ans(N, 0);

    for (int i = 0; i < N; i++) {
      rightSum -= rightCnt;
      rightCnt -= boxes[i] == '1';

      ans[i] = leftSum + rightSum;

      leftCnt += boxes[i] == '1';
      leftSum += leftCnt;
    }

    return ans;
  }
};