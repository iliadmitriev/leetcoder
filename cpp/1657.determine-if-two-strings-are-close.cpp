class Solution {
private:
    static const size_t N = 26;

public:
    bool closeStrings(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();

        if (n1 != n2) {
            return false;
        }

        vector<int> w1(N, 0), w2(N, 0);
        vector<bool> ex1(N, false), ex2(N, false); 

        for (int i = 0; i < n1; i++) {
            w1[word1[i] - 'a']++;
            w2[word2[i] - 'a']++;
            ex1[word1[i] - 'a'] = true;
            ex2[word2[i] - 'a'] = true;
        }

        std::sort(w1.begin(), w1.end());
        std::sort(w2.begin(), w2.end());

        return w1 == w2 && ex1 == ex2;
    }
};