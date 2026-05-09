import java.util.*;

class Solution {
    private static final int MOD = (int) 1e9 + 7;

    // Fast exponentiation: x^y mod MOD (binary exponentiation)
    private long pow(int x, int y) {
        long res = 1;
        long base = x % MOD;

        while (y > 0) {
            if ((y & 1) == 1) {  // Java: explicit comparison for bitwise result
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            y >>= 1;
        }
        return res;
    }

    // Modular inverse using Fermat's Little Theorem: x^(-1) ≡ x^(MOD-2) mod MOD
    private long inv(int x) {
        return pow(x, MOD - 2);
    }

    public int xorAfterQueries(int[] nums, int[][] queries) {
        final int n = nums.length;
        final int limit = (int) Math.sqrt(n) + 1;

        // Map: step size k → list of queries with that step (dense queries)
        Map<Integer, List<int[]>> dense = new HashMap<>();

        // q[0]=left, q[1]=right, q[2]=step, q[3]=value
        for (int[] q : queries) {
            if (q[2] >= limit) {
                // Sparse query: apply immediately (O(n/k) per query)
                for (int i = q[0]; i <= q[1]; i += q[2]) {
                    nums[i] = (int) ((1L * nums[i] * q[3]) % MOD);
                }
            } else {
                // Dense query: batch by step size for later processing
                dense.computeIfAbsent(q[2], k -> new ArrayList<>()).add(q);
            }
        }

        // Process batched dense queries using multiplicative difference array
        for (Map.Entry<Integer, List<int[]>> entry : dense.entrySet()) {
            int k = entry.getKey();
            List<int[]> qlist = entry.getValue();

            // mul[i] = cumulative multiplier to apply at index i
            int[] mul = new int[n];
            Arrays.fill(mul, 1);

            for (int[] q : qlist) {
                // Left bound: multiply by value
                mul[q[0]] = (int) ((1L * mul[q[0]] * q[3]) % MOD);

                // Right bound + step: divide by value (via modular inverse)
                int steps = (q[1] - q[0]) / k;
                int next = q[0] + (steps + 1) * k;
                if (next < n) {
                    mul[next] = (int) ((1L * mul[next] * inv(q[3])) % MOD);
                }
            }

            // Propagate multipliers along arithmetic progression with step k
            for (int i = 0; i < n; i++) {
                if (i >= k) {
                    mul[i] = (int) ((1L * mul[i] * mul[i - k]) % MOD);
                }
                nums[i] = (int) ((1L * nums[i] * mul[i]) % MOD);
            }
        }

        // Compute XOR of all elements (equivalent to std::accumulate with bit_xor)
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
}