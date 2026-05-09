#include <vector>
#include <algorithm>
using std::vector;

class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size(), m = queries.size();
        vector<int> prefix(n);

        std::partial_sum(arr.begin(), arr.end(), prefix.begin(), [](int a, int b) -> int {
            return a ^ b;
        });

        vector<int> res(m, 0);

        for (int i = 0; i < m; i++) {
            res[i] = prefix[queries[i][0]] ^ arr[queries[i][0]] ^prefix[queries[i][1]];
        }

        return res;
    }
};