#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  vector<string> getLongestSubsequence(vector<string> &words,
                                       vector<int> &groups) {
    vector<string> res({words.front()});
    int prev = groups.front();

    for (int i = 1; i < words.size(); i++) {
      if (groups[i] != prev) {
        res.push_back(words[i]);
        prev = groups[i];
      }
    }

    return res;
  }
};