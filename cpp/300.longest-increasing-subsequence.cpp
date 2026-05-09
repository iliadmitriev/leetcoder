class Solution {
private:
    int binSearchLeft(vector<int>& arr, int target) {
        int lo = 0, hi = arr.size();
        int mid;

        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        return lo;
    }

public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> st;
        st.reserve(nums.size());
        int ind;

        for (int num: nums) {
            if (st.empty() || num > st.back()) {
                st.push_back(num);
            }

            ind = binSearchLeft(st, num);
            st[ind] = num;
        }

        return st.size();
    }
};