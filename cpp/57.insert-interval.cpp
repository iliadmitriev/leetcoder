class Solution {
private:
  template <class T>
  int binarySearch(const vector<T> &arr, T &target,
                   function<bool(const T &, const T &)> cmp) {
    int l = 0, r = arr.size();
    int mid;
    while (l < r) {
      mid = (l + r) / 2;
      if (cmp(arr[mid], target)) {
        l = mid + 1;
      } else {
        r = mid;
      }
    }
    return l;
  }

public:
  vector<vector<int>> insert(vector<vector<int>> &intervals,
                             vector<int> &newInterval) {
    int ins = binarySearch<vector<int>>(
        intervals, newInterval,
        [&newInterval](auto &x, auto &y) -> bool { return x[0] < y[0]; });

    intervals.insert(intervals.begin() + ins, newInterval);
    vector<vector<int>> res;
    res.reserve(intervals.size());

    for (const auto &intv : intervals) {
      if (res.empty() || res.back()[1] < intv[0]) {
        res.push_back(intv);
      } else {
        res.back()[1] = max(res.back()[1], intv[1]);
      }
    }
    return res;
  }
};