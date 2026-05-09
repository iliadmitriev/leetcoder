class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        int i = 0; // target pointer
        int cur = 1;
        vector<string> res;

        while (i < target.size()) {
            res.push_back("Push");

            if (target[i] == cur) {
                i++;
            } else {
                res.push_back("Pop");
            }
            cur++;
        }
        return res;
    }
};