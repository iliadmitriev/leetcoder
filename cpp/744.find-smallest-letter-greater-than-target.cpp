class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int lo = 0; int hi = letters.size();
        int mid;
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (letters[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        if (lo == letters.size()) {
            return letters[0];
        }
        return letters[lo];
    }
};