class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        // Count min number of pigs.
        
        // b - number of buckets
        // T - number of rounds (minutesToTest / minutesToDie)
        // p - number of pigs
        // (T + 1) ^ p >= b
        // p = log(b) / log(T + 1)
        
        // answer is a ceil of p

        int pigs = 0;

        int states = minutesToTest / minutesToDie + 1;

        for (int i = 1; i < buckets; i *= states) {
            pigs++;
        }

        return pigs;
    }
};