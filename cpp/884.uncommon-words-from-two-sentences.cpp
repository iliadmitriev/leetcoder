#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::stringstream;
using std::unordered_map;
using std::vector;

class Solution {
public:
  vector<string> uncommonFromSentences(string s1, string s2) {
    unordered_map<string, int> words;
    vector<string> res;
    stringstream ss1(s1), ss2(s2);
    string word;

    for (int i = 0, j = 0; i <= s1.size(); i++) {
      if (i == s1.size() || s1[i] == ' ') {
        word = s1.substr(j, i - j);
        words[word]++;
        j = i + 1;
      }
    }

    for (int i = 0, j = 0; i <= s2.size(); i++) {
      if (i == s2.size() || s2[i] == ' ') {
        word = s2.substr(j, i - j);
        words[word]++;
        j = i + 1;
      }
    }

    for (auto [word, count] : words) {
      if (count == 1) {
        res.push_back(word);
      }
    }

    return res;
  }
};