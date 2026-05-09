#include <array>
#include <string>
#include <vector>

using std::string, std::vector, std::array;

class Solution {
public:
  vector<string> wordSubsets(vector<string> &words1, vector<string> &words2) {
    vector<string> res;
    array<int, 26> freq2{};

    for (string word : words2) {
      auto tmp{getFreqArr(word)};
      for (int i = 0; i < 26; i++) {
        freq2[i] = std::max(freq2[i], tmp[i]);
      }
    }

    for (string &word : words1) {
      const auto tmp{getFreqArr(word)};

      if (isSubset(tmp, freq2)) {
        res.push_back(word);
      }
    }

    return res;
  }

private:
  array<int, 26> getFreqArr(const string &word) {
    array<int, 26> freq{};
    for (char c : word) {
      freq[c - 'a']++;
    }
    return freq;
  }

  bool isSubset(const array<int, 26> &freq1, const array<int, 26> &freq2) {
    for (int i = 0; i < 26; i++) {
      if (freq1[i] < freq2[i]) {
        return false;
      }
    }
    return true;
  }
};