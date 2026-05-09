class Solution {
public:
    int kthGrammar(int n, int k) {
        int cur = 0;
        int left = 0; int right = 1 << (n - 1); int mid;
        for (int i = 1; i < n; i++) {
            mid = (left + right) / 2;
            // if k is greater than middle
            if (k > mid) {
                left = mid + 1; // go to the right
                cur = 1 - cur; // invert symbol
            } else {
                right = mid; // go to the left
            }
        }
        return cur;
    }
};