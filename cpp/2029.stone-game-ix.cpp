class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        // count the reminders left from division by 3
        // hint: c[0] - is a turn switch (even number can be discarded)
        // optimal sequnces when both players play optimally (symmetric)
        // seq 1: 11212121212...
        // seq 2: 22121212121...
        int c[3] = {0, 0, 0};
        for (int s : stones) {
            c[s % 3]++;
        }

        // c0 even or none
        if (c[0] % 2 == 0) {
            // for 1st player to win there should be both stones available
            return c[1] && c[2];
        }

        // c0 odd
        return c[1] - c[2] > 2 || c[2] - c[1] > 2;
    }
};