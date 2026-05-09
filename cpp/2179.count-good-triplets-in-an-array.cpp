#include <vector>

using std::vector;

class FenWick {
private:
  vector<int> data;

public:
  FenWick(int n) : data(n + 1, 0) {}

  void update(int idx, int val) {
    idx++;
    while (idx < data.size()) {
      data[idx] += val;
      idx += idx & -idx;
    }
  }

  int query(int idx) {
    idx++;
    int res = 0;
    while (idx > 0) {
      res += data[idx];
      idx -= idx & -idx;
    }
    return res;
  }
};

class Solution {
public:
  long long goodTriplets(vector<int> &nums1, vector<int> &nums2) {
    long count = 0;
    const int n = nums1.size();

    vector<int> pos2(n), reverseIndexMapping(n);
    for (int i = 0; i < n; i++) {
      pos2[nums2[i]] = i;
    }
    for (int i = 0; i < n; i++) {
      reverseIndexMapping[pos2[nums1[i]]] = i;
    }

    FenWick fenwick(n);
    for (int i = 0; i < n; i++) {
      int pos = reverseIndexMapping[i];
      int left = fenwick.query(pos);
      fenwick.update(pos, 1);

      int right = n - 1 - pos - i + left;

      count += long(left) * right;
    }

    return count;
  }
};