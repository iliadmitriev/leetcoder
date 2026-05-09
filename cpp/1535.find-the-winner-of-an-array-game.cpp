class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int curMax = arr[0];
        int curCnt = 0;

        for (int i = 1; i < arr.size(); i++) {
            if (curMax > arr[i]) {
                curCnt++;
            } else {
                curCnt = 1;
                curMax = arr[i];
            }

            if (curCnt == k) {
                return curMax;
            }
        }
        return curMax;
    }
};