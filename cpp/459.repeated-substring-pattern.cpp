class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        size_t n = s.size();
        
        for (int size = 1; size <= n / 2; size++) {
            if (n % size != 0)
                continue;
            
            bool full_match = true;
            for (int i = 0; i < n / size; i++) {
                if (s.substr(i * size, size) != s.substr(0, size)) {
                    full_match = false;
                    break;
                }
            }
            if (full_match)
                return true;
        }

        return false;
    }
};