#include <algorithm>
#include <cctype>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
  string mostCommonWord(string paragraph, vector<string> &banned) {
    std::unordered_set<string> bannedSet;
    for (string &ban : banned) {
      std::transform(ban.begin(), ban.end(), ban.begin(), ::tolower);
      bannedSet.insert(ban);
    }

    int i = 0, j = 0, n = paragraph.size();

    std::unordered_map<string, int> wordCount;

    while (i < n) {

      while (i < n && !isalpha(paragraph[i]))
        i++;

      j = i;

      while (j < n && isalpha(paragraph[j]))
        j++;

      if (j > i) {
        string word = paragraph.substr(i, j - i);
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);

        if (!bannedSet.count(word)) {
          wordCount[word]++;
        }
      }

      i = j;
    }

    string maxWord = wordCount.begin()->first;
    int maxCount = wordCount.begin()->second;

    for (auto &[k, v] : wordCount) {
      if (v > maxCount) {
        maxCount = v;
        maxWord = k;
      }
    }

    return maxWord;
  }
};