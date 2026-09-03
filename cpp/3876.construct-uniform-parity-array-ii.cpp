class Solution {
public:
    bool uniformArray(vector<int>& nums1) {

        int odd = 0, even = 0, minOdd = -1, min = -1;

        for (int v : nums1) {
          if (v & 1) {
            odd++;
            if (minOdd == -1 || v < minOdd) {
              minOdd = v;
            }
          } else {
            even++;
          }

          if (min == -1 || v < min) {
            min = v;
          }
        }

        // the array parity is the same (all the number ether even or odd)
        if (odd == 0 || even == 0) {
          return true;
        }

        // the array is the mixture of the odd and even numbers
        // in this case we can't make the array all even
        // because, but to make the smallest odd number even by subtraction
        // we need even more smaller number which is impossible
        // therefore, there is only chance to make the array parity odd
        // by subtracting the smallest odd number from all the even
        // but again to comply with the condition (>=1) it should be the smallest one.
        return minOdd == min;
        
    }
};