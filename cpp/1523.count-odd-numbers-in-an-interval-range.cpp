class Solution {
public:
  int countOdds(int low, int high) {
    // odd numbers inclusive between 0 and x is (x+1)/2
    // odd numbers exclusive between 0 and x is x/2
    return (high + 1) / 2 - low / 2;
  }
};