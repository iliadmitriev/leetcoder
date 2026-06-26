class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        const int n = nums.size();
        long long res = 0;

        int pre = n + 1;                   // [-n;+n] shifted to [1;2*n+1] (n + 1 is a real 0)
        vector<int> cnt(2 * n + 2, 0); // prefix frequencies
        vector<int> acc(2 * n + 2, 0); // accumulated prefix frequencies,
        // acc[k] = sum_i(cnt[i]), 0 <= i <= k

        cnt[pre]++; // pre[0] = 1
        acc[pre]++; // acc[0] = 1

        for (int num : nums) {
          pre += num == target ? +1 : -1;
          
          // add prefix count
          cnt[pre]++; 
          // update acc[pre], 
          // get previous accumulated prefix of length - 1
          // add current prefix frequency
          acc[pre] = acc[pre - 1] + cnt[pre]; 

          res += acc[pre - 1]; // not inclusive (get previous)
        }

        return res;
    }
};