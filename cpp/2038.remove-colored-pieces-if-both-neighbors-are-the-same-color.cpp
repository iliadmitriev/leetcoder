class Solution {
public:
    bool winnerOfGame(string colors) {
        int a=0,b=0;
        int l=0,r=0;

        while (l < colors.size()) {
            while (r < colors.size() && colors[r] == colors[l]) {
                r++;
            }

            if (colors[l] == 'A') {
                a += max(0, r - l - 2);
            } else {
                b += max(0, r - l - 2);
            }

            l = r;
        }

        return a > b;
    }
};