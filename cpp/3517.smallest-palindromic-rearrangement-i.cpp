#include <string>
#include <array>

using std::string;

class Solution {
public:
    string smallestPalindrome(string s) {
       const int n = s.size();
       const int mid = n / 2;

       std::array<int, 26>cnt = {0};

       for (int i = 0; i < n / 2; i++) {
          cnt[s[i] - 'a']++;
       }

       string ss;
       ss.reserve(n);

       for (int j = 0; j < 26; j++) {
          ss.append(cnt[j], 'a' + j);
       }
       
       if (n % 2) {
        ss.push_back(s[mid]);
       }

       for (int j = 25; j >= 0; j--) {
         ss.append(cnt[j], 'a' + j);
       }

      return ss;
    }
};