class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        int prev = 0;
        for (int num : arr) {
            prev = min(prev + 1, num);
        }
        return prev;
    }
};