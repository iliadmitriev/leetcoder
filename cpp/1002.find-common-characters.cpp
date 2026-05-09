#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  vector<int> count(string &word) {
    vector<int> res(26, 0);
    for (char c : word) {
      res[c - 'a']++;
    }
    return res;
  }

public:
  vector<string> commonChars(vector<string> &words) {
    vector<string> res;

    vector<int> total = count(words[0]);

    for (int i = 1; i < words.size(); i++) {
      vector<int> word = count(words[i]);

      for (int j = 0; j < 26; j++) {
        total[j] = std::min(total[j], word[j]);
      }
    }

    for (int i = 0; i < 26; i++) {
      for (int j = 0; j < total[i]; j++) {
        res.push_back(string(1, i + 'a'));
      }
    }

    return res;
  }
};