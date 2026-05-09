class Solution {
public:
  int findComplement(int num) {
    return (long(1 << (32 - __builtin_clz(num))) - 1) ^ num;
  }
};