class Solution {
private:
    int left(const vector<int>& arr, int target) {
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
        return lo;
    }

    int right(const vector<int>& arr, int target) {
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
        return lo;
    }
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end(), std::less<int>());
        int lo = left(nums, target);
        int hi = right(nums, target);
        vector<int> res;
        for (int i = lo; i < hi; i++) {
            res.push_back(i);
        }
        return res;
    }
};