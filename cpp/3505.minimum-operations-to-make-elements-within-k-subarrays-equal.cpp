#include <queue>
#include <unordered_map>
#include <vector>

using std::vector, std::priority_queue, std::unordered_map;

class BalancedWindow {
private:
    int size;
    long long lower_sum;
    long long upper_sum;
    // soft lazy delete array for both queue
    unordered_map<int, int> removed;
    // need to store the real size (considering the removed elements)
    int lower_size;
    int upper_size;
    priority_queue<int, vector<int>, less<>> lower;
    priority_queue<int, vector<int>, greater<>> upper;

    // clean deleted values from queue q
    template <typename Q> void prune(Q& q) {
        while (q.size() && removed.contains(q.top())) {
            int top = q.top();
            q.pop();
            removed[top]--;
            if (removed[top] <= 0) {
                removed.erase(top);
            }
        }
    }

    void rebalance() {
        if (lower_size > upper_size + 1) {
            int val = lower.top();
            lower.pop();
            lower_sum -= val;
            --lower_size;
            upper.push(val);
            upper_sum += val;
            ++upper_size;
            prune(lower);
        } else if (lower_size < upper_size) {
            int val = upper.top();
            upper.pop();
            upper_sum -= val;
            --upper_size;
            lower.push(val);
            lower_sum += val;
            ++lower_size;
            prune(upper);
        }
    }

public:
    BalancedWindow()
        : lower_sum{0LL}, upper_sum{0LL}, lower_size{0}, upper_size{0}, lower(),
          upper() {}

    void add(int val) {

        if (!lower_size || val <= lower.top()) {
            lower.push(val);
            lower_sum += val;
            ++lower_size;
        } else {
            upper.push(val);
            upper_sum += val;
            ++upper_size;
        }

        rebalance();
    }
    void remove(int val) {
        removed[val]++;

        if (val <= lower.top()) {
            lower_sum -= val;
            --lower_size;
            prune(lower);
        } else {
            upper_sum -= val;
            --upper_size;
            prune(upper);
        }

        rebalance();
    }

    long long get_ops() {
        long long mid = lower.top();
        return upper_sum - lower_sum + mid * (lower_size - upper_size);
    }
};

class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        const int n = nums.size();

        BalancedWindow win;
        vector<long long> ops(n);

        for (int r = 0; r < n; r++) {
            win.add(nums[r]);

            int l = r - x + 1;
            if (l < 0) {
                continue;
            }

            ops[r] = win.get_ops();
            win.remove(nums[l]);
        }

        vector<vector<long long>> dp(n, vector<long long>(k + 1, LLONG_MAX));

        for (int i = 0; i < n; i++) {
            dp[i][0] = 0;
        }
        for (int j = 1; j <= k; j++) {
            if (j == 1) {
                dp[x - 1][j] = ops[x - 1];
            } else {
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + ops[j * x - 1];
            }
        }
        for (int j = 1; j <= k; j++) {
            for (int i = j * x; i < n; i++) {
                dp[i][j] = min(dp[i - x][j - 1] + ops[i], dp[i - 1][j]);
            }
        }

        return dp[n - 1][k];
    }
};