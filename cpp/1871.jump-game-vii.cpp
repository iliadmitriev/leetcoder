#include <vector>

class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        const int n = s.size();

        if (s[n - 1] == '1') {
            return false;
        }

        std::queue<int> q;

        int seen = 0;
        q.push(0);

        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            int start = std::max(seen, cur + minJump); // cutoff seen values
            int end = std::min(n, cur + maxJump + 1); // cutoff the end of array

            // iterate all possible next values
            for (int nxt = start; nxt < end; nxt++) {
                if (s[nxt] == '1') {
                    continue;
                }

                if (nxt == n - 1) {
                    return true;
                }

                q.push(nxt);
            }

            seen = end;
        }

        return false;
    }
};