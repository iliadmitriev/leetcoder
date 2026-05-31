#include <algorithm>
#include <vector>

using std::vector;

class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        long long total = mass;
        int h = 0;

        for (int ast : asteroids) {
            if (ast <= total) {
                total += ast;
            } else {
                asteroids[h++] = ast;
            }
        }

        std::ranges::sort(asteroids.begin(), asteroids.begin() + h);

        for (int i = 0; i < h; i++) {
            if (asteroids[i] > total) {
                return false;
            }

            total += asteroids[i];
        }

        return true;
    }
};