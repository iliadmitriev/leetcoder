class Solution {
  // static int bisectRight(int[] arr, int x, int lo) {
  //   int hi = arr.length;
  //   int res = 0;
  //   int mid;

  //   while (lo < hi) {
  //     mid = (lo + hi) / 2;

  //     if (arr[mid] >= x) {
  //       res = mid;
  //       lo = mid + 1;
  //     } else {
  //       hi = mid;
  //     }
  //   }

  //   return res;
  // }

  public int maxDistance(int[] nums1, int[] nums2) {
    int maxDist = 0;
    int i = 0, j = 0;
    final int m = nums1.length, n = nums2.length;

    while (i < m && j < n) {
      if (nums1[i] <= nums2[j]) {
        maxDist = Math.max(maxDist, j - i);
        j++;
      } else {
        i++;
        j++;
      }
    }

    return maxDist;
  }
}