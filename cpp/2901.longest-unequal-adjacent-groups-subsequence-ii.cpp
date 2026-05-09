#include <string>
#include <vector>

using std::string, std::vector;

class Solution {
public:
  vector<string> getWordsInLongestSubsequence(vector<string> &words,
                                              vector<int> &groups) {
    const int n = words.size();
    vector<int> dp(n, 1);
    vector<int> prev(n, -1);
    int maxLen = 1, maxIdx = 0;
    vector<string> res;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if (groups[i] == groups[j] || words[i].size() != words[j].size() ||
            hammingDistance(words[i], words[j]) != 1) {
          continue;
        }

        if (dp[i] < dp[j] + 1) {
          dp[i] = dp[j] + 1;
          prev[i] = j;
        }
      }

      if (dp[i] > maxLen) {
        maxLen = dp[i];
        maxIdx = i;
      }
    }

    while (maxIdx != -1) {
      res.push_back(words[maxIdx]);
      maxIdx = prev[maxIdx];
    }
    std::reverse(res.begin(), res.end());

    return res;
  }

private:
  int hammingDistance(const string &s1, const string &s2) {
    int res = 0;
    for (int i = 0; i < s1.size(); i++) {
      if (s1[i] != s2[i]) {
        res++;
      }
    }
    return res;
  }
};