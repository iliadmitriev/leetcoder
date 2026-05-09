class Solution {
private:
  // returns:
  //  count of fractions less than val
  //  index of the numerator of the largest fraction less than val
  //  index of the denominator of the largest fraction less than val
  tuple<int, int, int> countFracLess(const vector<int> &arr, float val) {
    int n = arr.size(), count = 0;
    int p = 0, q = n - 1, i = 0, j = 1;
    float maxFraction = float(arr[p]) / float(arr[q]);

    for (; i < n - 1; i++) {
      for (; j<n &&float(arr[i]) / float(arr[j])> val; j++)
        ;

      if (j == n)
        break;

      if (maxFraction < float(arr[i]) / float(arr[j])) {
        maxFraction = float(arr[i]) / float(arr[j]);
        p = i;
        q = j;
      }

      count += n - j;
    }

    return {count, p, q};
  }

public:
  vector<int> kthSmallestPrimeFraction(vector<int> &arr, int k) {
    int n = arr.size();
    float low = 0.0, high = 1.0;
    float mid;

    while (low < high) {
      mid = (low + high) / 2.0;
      auto [count, p, q] = countFracLess(arr, mid);

      if (count == k) {
        return {arr[p], arr[q]};
      } else if (count < k) {
        low = mid;
      } else {
        high = mid;
      }
    }

    return {arr[0], arr[n - 1]};
  }
};