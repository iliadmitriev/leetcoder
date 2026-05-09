class Solution {
public:
    int climbStairs(int n) {
        int prev = 0, cur = 1;
        int tmp;
        
        for (; n > 0; n--) {
            tmp = prev;
            prev = cur;
            cur = tmp + cur;
        }

        return cur;
    }
};