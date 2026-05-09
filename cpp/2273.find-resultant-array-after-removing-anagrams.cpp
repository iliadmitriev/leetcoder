#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
private:
  vector<int> makeKey(const string &s) {
    vector<int> freq(26, 0);
    for (char c : s) {
      freq[c - 'a']++;
    }
    return freq;
  }

public:
  vector<string> removeAnagrams(vector<string> &words) {
    vector<int> prevKey;
    vector<string> res;

    for (const string &word : words) {
      auto key = makeKey(word);
      if (key != prevKey) {
        res.push_back(word);
        prevKey = key;
      }
    }

    return res;
  }
};