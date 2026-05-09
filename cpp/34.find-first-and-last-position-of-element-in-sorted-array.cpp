class Solution {
private:
    int left(vector<int>& arr, int target) {
        int lo = 0;
        int hi = arr.size();
        int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        if (lo < arr.size() && arr[lo] == target) {
            return lo;
        }
        return -1;
    }
    int right(vector<int>& arr, int target) {
        int lo = 0;
        int hi = arr.size();
        int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (arr[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        if (lo - 1 >= 0 && arr[lo - 1] == target) {
            return lo - 1;
        }
        return -1;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return {left(nums, target), right(nums, target)};
    }
};