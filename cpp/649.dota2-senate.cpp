class Solution {
public:
    string predictPartyVictory(string senate) {
        int r = 0, d = 0,
            ban_r = 0, ban_d = 0;

        
        queue<char> que;

        for (char sen : senate) {
            que.push(sen);
            if (sen == 'R') {
                r++;
            } else {
                d++;
            }
        }

        while (!senate.empty()) {
            char sen = que.front(); que.pop();

            if (sen == 'R' && r > 0) {
                if (ban_r > 0) {
                    ban_r--;
                    continue;
                }

                if (d > 0) {
                    d--;
                    ban_d++;
                    que.push(sen);
                    continue;
                }

                return string("Radiant");

            } else if (sen == 'D' && d > 0) {
                if (ban_d > 0) {
                    ban_d--;
                    continue;
                }

                if (r > 0) {
                    r--;
                    ban_r++;
                    que.push(sen);
                    continue;
                }
                return string("Dire");
            }
        }

        return d > 0 && ban_d == 0 ? string("DDD") : string("RRR");
    }
};