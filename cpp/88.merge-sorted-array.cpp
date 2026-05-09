/*

1. inverse problem:
instead of trying to build smaller to greater from the beggining of array
try to build greater to smaller from the end of the array 

k = insert point starging from end of the result moving to the beggining
i = read point from ten end of nums1
j = read point from the end of nums2
             i     k
nums1 = [1,2,3,0,0,0]
             j
nums2 = [2,5,6]

*/
#include <vector>
using std::vector;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      int k = m + n - 1;
      int i = m - 1, j = n - 1;

      while (i >= 0 && j >= 0) {
        if (nums1[i] >= nums2[j]) {
          nums1[k--] = nums1[i--];
        } else {
          nums1[k--] = nums2[j--];
        }
      }

      while (j >= 0) {
        nums1[k--] = nums2[j--];
      }
    }
};