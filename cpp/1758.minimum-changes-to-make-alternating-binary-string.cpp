class Solution {
public:
    int minOperations(string s) {
      int parity = 1;
      int even = 0;

      for (char ch : s) {
        int d = ch - '0';

        if (d != parity) {
          even++;
        }

        parity = 1 - parity;
      }

      return std::min(even, int(s.size()) - even);
    }
};