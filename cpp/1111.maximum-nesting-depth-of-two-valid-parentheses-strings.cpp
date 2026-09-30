#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        const int n = seq.size();
        vector<int> res(n, -1);
        int depth = 0;

        for (int i = 0; i < n; i++) {
            switch (seq[i]) {
            case '(':
                depth = 1 - depth;
                res[i] = depth;
                break;
            case ')':
                res[i] = depth;
                depth = 1 - depth;
            }
        }

        return res;
    }
};