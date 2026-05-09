class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int w1 = 0;
        int w2 = 0;
        auto c1 = word1[w1].begin();
        auto c2 = word2[w2].begin();
        bool flag = true;

        int n1 = word1.size();
        int n2 = word2.size();

        while (w1 < n1 && w2 < n2) {

            if (*c1 != *c2) {
                flag = false; break;
            }

            c1++;
            c2++;

            if (c1 == word1[w1].end()) {
                w1++;
                if (w1 < n1) {
                    c1 = word1[w1].begin();
                }
            }
            if (c2 == word2[w2].end()) {
                w2++;
                if (w2 < n2) {
                    c2 = word2[w2].begin();
                }
            }
        }

        if (flag) {
            flag = (w1 == n1) && (w2 == n2);
        }

        return flag;
    }
};