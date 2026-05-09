class Solution {
public:
  vector<int> singleNumber(vector<int> &nums) {
    int firstSecond = 0, first = 0;

    for (auto num : nums) {
      firstSecond ^= num;
    }

    // get first bit where num1 and num2 differ
    // it can be arbitrary, but we use first rightmost bit
    int mask = firstSecond & (~long(firstSecond) + 1);

    // use this bit to separate nums into two groups
    for (auto num : nums) {
      if (num & mask)
        first ^= num;
    }

    return {first, firstSecond ^ first};
  }
};