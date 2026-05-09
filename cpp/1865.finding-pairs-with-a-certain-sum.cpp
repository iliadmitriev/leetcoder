#include <unordered_map>
#include <vector>
using std::vector, std::unordered_map;

class FindSumPairs {
public:
  FindSumPairs(vector<int> &nums1, vector<int> &nums2) : nums2(nums2) {
    for (int v : nums1) {
      m1[v]++;
    }

    for (int v : nums2) {
      m2[v]++;
    }
  }

  void add(int index, int val) {
    m2[nums2[index]]--;
    nums2[index] += val;
    m2[nums2[index]]++;
  }

  int count(int tot) {
    int total = 0;

    for (auto [k1, c1] : m1) {
      if (m2.find(tot - k1) != m2.end()) {
        total += c1 * m2[tot - k1];
      }
    }

    return total;
  }

private:
  unordered_map<int, int> m1;
  unordered_map<int, int> m2;
  vector<int> &nums2;
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */