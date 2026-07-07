#include <vector>

class Solution {
public:
    long long sumAndMultiply(int n) {
        long long sum = 0;
        long long x = 0;
        std::vector<int> v;

        while (n) {
            if (n % 10 != 0) {
                sum += n % 10;
                v.push_back(n % 10);
            }

            n /= 10;
        }

        while (!v.empty()) {
            x *= 10;
            x += v.back();

            v.pop_back();
        }

        return x * sum;
    }
};