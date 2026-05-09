#include <cctype>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  vector<int> keyFunc(const string &key) {
    vector<int> ret(26, 0);

    for (char ch : key) {
      if (isalpha(ch)) {
        ret[tolower(ch) - 'a']++;
      }
    }

    return ret;
  }

  bool compareFunc(const vector<int> &key1, const vector<int> &key2) {
    for (int i = 0; i < 26; i++) {
      if (key1[i] > key2[i]) {
        return false;
      }
    }
    return true;
  }

public:
  string shortestCompletingWord(string licensePlate, vector<string> &words) {

    auto plate = keyFunc(licensePlate);
    int minLen = 1000;
    string result;

    for (const string &w : words) {
      if (compareFunc(plate, keyFunc(w)) && w.size() < minLen) {
        minLen = std::min(minLen, int(w.size()));
        result = w;
      }
    }

    return result;
  }
};