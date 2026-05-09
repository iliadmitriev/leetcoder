class Solution {
public:
    vector<int> countBits(int n) {
        int l = n + 1;
        vector<int> res(l, 0);

        for (int i = 1; i < l; i++) {
            res[i] = res[i & (i - 1)] + 1;
        }

        return res;
    }
};