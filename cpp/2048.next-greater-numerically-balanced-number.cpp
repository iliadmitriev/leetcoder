#include <cmath>
#include <vector>
using std::vector;

class BeatufilNum {
private:
  vector<int> beatiful;

  // gen - generate all beautiful numbers with m digits and save them
  void gen(int i, int cur, int m, vector<int> &voc) {
    if (i == m) {
      if (check(voc)) {
        beatiful.push_back(cur);
        return;
      }
    }

    for (int d = 1; d <= m; d++) {
      // if digit d is fulfilled or not much space left for digit to fulfill
      if (voc[d] == d || voc[d] + m - i < d) {
        continue;
      }

      voc[d]++;
      gen(i + 1, cur * 10 + d, m, voc);
      voc[d]--;
    }
  }

  // check vocabulary empty and which means all digits is consumed and number is
  // beatuful
  bool check(const vector<int> &voc) {
    for (int i = 0; i < 10; i++) {
      if (voc[i] == i || voc[i] == 0) {
        continue;
      }
      return false;
    }
    return true;
  }

public:
  BeatufilNum(int n) {
    int m;
    if (n) {
      m = std::log10(n) + 1;
    } else {
      m = 1;
    }

    vector<int> voc1(10, 0);
    gen(0, 0, m, voc1);

    vector<int> voc2(10, 0);
    gen(0, 0, m + 1, voc2); // generate with overlap
  }

  // binary search bisect with right bias
  int find(int target) {
    int lo = 0, hi = beatiful.size();
    int mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (beatiful[mid] > target) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return beatiful[lo];
  }
};

class Solution {
public:
  int nextBeautifulNumber(int n) {
    BeatufilNum beatufilNum(n);

    return beatufilNum.find(n);
  }
};