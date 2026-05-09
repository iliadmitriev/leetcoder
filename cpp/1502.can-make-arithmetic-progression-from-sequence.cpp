class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        auto it1 = arr.begin();
        auto it2 = it1 + 1;
        int step = *it2 - *it1;

        for (; it2 != arr.end(); it1++, it2++) {
            if (step != *it2 - *it1) {
                return false;
            }
        }
        return true;
    }
};