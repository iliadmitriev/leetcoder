class Solution {
private:
    vector<vector<int>> res;
    vector<int> curr;

    void backtrack(int first, int n, int k) {
        if ( curr.size() == k ) {
            res.push_back(curr);
            return;
        }

        for (int i = first; i <= n; i++) {
            curr.push_back(i);
            backtrack(i + 1, n, k);
            curr.pop_back();

        }

    }

public:
    vector<vector<int>> combine(int n, int k) {
        backtrack(1, n, k);
        return res;
    }
};