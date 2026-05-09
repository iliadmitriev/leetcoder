const int MOD = 1e9 + 7;

class Solution {
private:
    int rev(int x) {
        int y = 0;
        while (x > 0) {
            y *= 10;
            y += x % 10;
            x /= 10;
        }
        return y;
    }
public:
    int countNicePairs(vector<int>& nums) {
        long count = 0;
        unordered_map<int, int> freq;
        for (auto num : nums) {
            freq[num - rev(num)]++;
        }

        for (auto [_, v] : freq) {
            count += long(v) * (v - 1) / 2;
        }
        return count % MOD;
    }
};