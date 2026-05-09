class Solution {
public:
    int minOperations(vector<int>& arr, int k) {

        vector<int> ans(k + 1, -1);
        int count = 0;
        int j = 1;
        
        for (int i = arr.size() - 1; i >= 0 && j <= k; i--) {
            if (arr[i] <= k && ans[arr[i]] != 1) {
                ans[arr[i]] = 1;
                j++;
                count++;
            } else {
                count++;
            }
        }

        return count;
    }
};
