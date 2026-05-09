#include <iostream>
#include <vector>

static const int ZERO = []() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

using std::vector;
class Solution {
public:
  vector<int> findThePrefixCommonArray(vector<int> &A, vector<int> &B) {
    const int N = A.size();
    vector<int> cache(N + 1, 0);
    vector<int> C(N, 0);
    int count = 0;

    for (int i = 0; i < N; ++i) {
      cache[A[i]]++;
      count += cache[A[i]] == 2;

      cache[B[i]]++;
      count += cache[B[i]] == 2;

      C[i] = count;
    }

    return C;
  }
};