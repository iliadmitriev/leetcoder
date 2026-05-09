#include <cstring>
#include <string>
using std::string;

class Solution {
private:
  bool strcmp(const string &s, int i, int j, int size) {
    const int limit = s.size();

    for (int k = 0; k < size; k++) {
      if (i + k >= limit) {
        return false;
      } else if (j + k >= limit) {
        return true;
      } else if (s[i + k] != s[j + k]) {
        return s[i + k] > s[j + k];
      }
    }

    return false;
  }

public:
  string answerString(string word, int numFriends) {
    if (numFriends == 1) {
      return word;
    }

    const int n = word.size();
    const int m = n - numFriends + 1; // window size
    int j = 0; // current string lexicographical largest index

    for (int i = 0; i < n; i++) {
      if (strcmp(word, i, j, m)) {
        j = i;
      }
    }

    return word.substr(j, m);
  }
};