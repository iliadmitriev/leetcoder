class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.size() != goal.size()) {
            return false;
        }

        string db = s + s;

        // O(m + n), if m == n, O(n + n) => O(n)
        return db.find(goal) != string::npos;
    }
};