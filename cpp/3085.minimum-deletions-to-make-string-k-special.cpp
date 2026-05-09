#include <array>
#include <numeric>
#include <string>

using std::string, std::array;

class Solution {
public:
  int minimumDeletions(string word, int k) {
    const int N = 26;
    array<int, N> cnt = {0};

    for (char c : word) {
      cnt[c - 'a']++;
    }

    std::sort(cnt.begin(), cnt.end());

    // find the first non-zero element
    int start = 0;
    while (start < N && cnt[start] == 0) {
      start++;
    }

    int minDeletions = std::accumulate(cnt.begin(), cnt.end(), 0);

    for (int i = start; i < N; i++) {
      int curDeletions = 0;

      for (int j = start; j < N; j++) {
        if (cnt[j] < cnt[i]) {
          curDeletions += cnt[j];
        } else {
          curDeletions += std::max(0, cnt[j] - (cnt[i] + k));
        }
      }

      minDeletions = std::min(minDeletions, curDeletions);
    }

    return minDeletions;
  }
};