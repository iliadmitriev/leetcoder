class Solution {
private:
    bool check(vector<int> arr) {
        sort(arr.begin(), arr.end());
        for (int i = 1; i < arr.size() - 1; i++) {
            if (arr[i - 1] - arr[i] != arr[i] - arr[i + 1]) {
                return false;
            }
        }
        return true;
    }
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        int n = min(l.size(), r.size());

        vector<bool> res(n, false);
        for (int i = 0; i < n; i++) {
            res[i] = check(vector<int>(nums.begin() + l[i], nums.begin() + r[i] + 1));
        }

        return res;
    }
};