#include <cmath>
#include <functional> // std::bit_xor
#include <numeric>    // std::accumulate
#include <unordered_map>
#include <vector>

using std::vector, std::unordered_map;

class Solution {
private:
    static const int MOD = int(1e9) + 7;

    // exponentiate x ^ y modulo MOD
    long long pow(int x, int y) {
        long long res = 1;
        long long base = x % MOD;

        while (y > 0) {
            if (y & 1) {
                res = (res * base) % MOD;
            }

            base = (base * base) % MOD;
            y >>= 1;
        }

        return res;
    }

    // invert x => 1 / x modulo MOD
    // Fermat little theoreme:
    //        x ^ (p - 1) = 1 mod p
    // Divide both sides by x:
    //        x ^ (p - 2) = 1 / x
    long long inv(int x) { return pow(x, MOD - 2); }

public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        const int n = nums.size();
        const int limit = std::sqrt(n) + 1;
        unordered_map<int, vector<vector<int>>> dense; // group by step size

        // q(0 - left, 1 - right, 2 - step, 3 - value)
        for (auto& q : queries) {
            if (q[2] >= limit) { // if sparse
                // apply adhoc: multiply by value each number left to right
                // (inclusive) with step
                for (int i = q[0]; i <= q[1]; i += q[2]) {
                    nums[i] = (1LL * nums[i] * q[3]) % MOD;
                }
            } else { // if dense
                // save for later grouping by step size
                dense[q[2]].push_back(q);
            }
        }


        // apply dense rows according to step size k
        for (auto& [k, qlist] : dense) {
            // multiply vector;
            vector<int> mul(n, 1);
            
            for (auto& q : qlist) {
                // left bound multiply
                mul[q[0]] = (1LL * mul[q[0]] * q[3]) % MOD;
                // next to right bound
                int steps = (q[1] - q[0]) / k;     // number of steps
                int next = q[0] + (steps + 1) * k; // next step index

                // right bound divide by (if withing a bounds)
                if (next < n) {
                    mul[next] = (1LL * mul[next] * inv(q[3])) % MOD;
                }
            }

            for (int i = 0; i < n; i++) {
                if (i >= k) {
                    mul[i] = (1LL * mul[i] * mul[i - k]) % MOD;
                }
                nums[i] = (1LL * nums[i] * mul[i]) % MOD;
            }
        }

        return std::accumulate(nums.begin(), nums.end(), 0,
                               std::bit_xor<int>());
    }
};