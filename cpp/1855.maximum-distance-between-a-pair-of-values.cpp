class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int maxDist = 0;

        for (int i = 0, j = 0; i < nums1.size(); i++) {
            j = bisectRight(nums2, nums1[i], i);
            maxDist = std::max(maxDist, j - i);
        }

        return maxDist;
    }

private:
    int bisectRight(vector<int>& arr, int x, int lo) {
        int mid, res = 0, hi = arr.size();

        while (lo < hi) {
            mid = (lo + hi) / 2;
            // [100,20,*10*,10,5] 55
            if (arr[mid] >= x) {
                lo = mid + 1;
                res = mid;
            } else {
                hi = mid;
            }
        }

        return res;
    }
};