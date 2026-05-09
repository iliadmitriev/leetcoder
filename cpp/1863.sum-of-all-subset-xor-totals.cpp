class Solution {

public:
  int subsetXORSum(vector<int> &nums) {
    /*
            Set of size n, will have 2^n subsets.

            In each element from base set is included
            or not in each subset (binary).

            Each element included in 2^(n - 1) subsets
            (half of all possible subsets).

            Xor operation works: even number of 1s = 0, odd number of 1s = 1.

            Since each element (each bit of element) is included 2^(n - 1)
            number of times (even), we can assume than first less significant
            n - 1 bits of the result will be always 0.

            if any bit is set in any of elemenst from base set nums,
            it will be added to the result 2^(n - 1) times.

            So given all of this, we find all the bits
            that is set to 1 in the base set nums. (OR)
            And then shift it to the left n - 1 times.
    */

    int totalSum = reduce(nums.begin(), nums.end(), 0, bit_or<>());

    return totalSum << (nums.size() - 1);
  }
};