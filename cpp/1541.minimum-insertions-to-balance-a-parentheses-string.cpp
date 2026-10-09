#include <string>
using std::string;

class Solution {
public:
    int minInsertions(string s) {
        int res = 0, closingNeeded = 0;

        for (char ch : s) {
            switch (ch) {
            case '(':
                closingNeeded += 2;

                if (closingNeeded % 2) { // closing is not even
                    closingNeeded--;
                    res++;
                }
                break;

            case ')':
                closingNeeded--;

                if (closingNeeded < 0) { // if extra closing parenthesis
                    res++;               // insert opening parenthesis
                    closingNeeded += 2;  // increase closing needed by 2
                }
            }
        }

        return res + closingNeeded;
    }
};