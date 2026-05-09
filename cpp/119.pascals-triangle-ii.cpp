class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int n = rowIndex + 1;
        vector<int> res(n);
        long curr = 1;
        res[0] = curr;

        for (auto i = 1; i < n; i++) {
            curr *= n - i;
            curr /= i;
            res[i] = curr;
        }

        return res;
    }
};