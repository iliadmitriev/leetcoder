class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        bitset<101> s;

        for (int n : nums) {
          if (n % k == 0) {
            s.set(n / k - 1);
          }
        }

        s.flip();
        int pos = s._Find_first() + 1;

        return pos * k;
    }
};