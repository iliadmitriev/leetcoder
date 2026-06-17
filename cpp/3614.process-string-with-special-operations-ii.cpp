class Solution {
public:
    char processStr(string s, long long k) {
        long long size = 0;

        // simulate forward
        for (char ch : s) {
            if (ch == '*') {
                size = std::max(0LL, size - 1); // remove symbol if exists
            } else if (ch == '#') {
                size *= 2; // double tape size
            } else if (ch == '%') {
                // reverse tape (length does not change)
            } else {
                size++; // add one symbol to tape
            }
        }

        // check if tape length reached k
        if (k >= size) {
            return '.'; // tape is shorter than k
        }

        // simulate backward
        for (char ch : std::views::reverse(s)) {

            if (ch == '*') {
                size++; // reverse deletion

            } else if (ch == '#') {
                long long half = size / 2; // reverse doubling

                if (k >= half) {
                    k -= half; // second half
                }

                size = half;

            } else if (ch == '%') {
                // inverse reverse
                // recalculate position from last
                k = size - 1 - k;
            } else {                 // if character
                if (size - 1 == k) { // check if it's position is k
                    return ch;       // found, return
                }

                size--; // reduce size
            }
        }

        return '.'; // default identity value
    }
};