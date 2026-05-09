class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();

        int res = arr[0];
        int count = 1;

        for (int i = 1; i < n; i++) {
            if (arr[i - 1] == arr[i]) {
                count++;
            } else {
                count = 1;
            }

            if (count > n / 4) {
                res = arr[i];
                break;
            }
        }

        return res;
    }
};