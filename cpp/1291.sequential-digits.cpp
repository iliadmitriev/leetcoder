class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        queue<int> q;
        for (int i = 1; i < 10; i++) { q.push(i); }

        vector<int> res;

        while (!q.empty()) {
            int num = q.front(); q.pop();

            if (low <= num && num <= high) {
                res.push_back(num);
            }

            int digit = num % 10 + 1;

            if (digit < 10) {
                q.push(num * 10 + digit);
            }
        }

        return res;
    }
};