class Solution {
public:
    int minDeletions(string s) {
        int n = 26;

        vector<int> freq(n, 0);
        for (char ch : s) {
            freq[ch - 'a']++;
        }
        sort(freq.begin(), freq.end(), greater<int>());
        for (auto fr : freq) { cout << fr << " ";}
        cout << endl;

        int deletions = 0;
        // && freq[i] !=0 && freq[i + 1] != 0;
        for (int i = 0; i < n - 1; i++) {
            if (freq[i] == 0 && freq[i] <= freq[i + 1]) {
                auto diff = freq[i + 1] - freq[i];
                deletions += diff;
                freq[i + 1] -= diff;
            } else if (freq[i] <= freq[i + 1]) {
                auto diff = 1 + freq[i + 1] - freq[i];
                deletions += diff;
                freq[i + 1] -= diff;
            }
        }

        for (auto fr : freq) { cout << fr << " ";}

        return deletions;

    }
};