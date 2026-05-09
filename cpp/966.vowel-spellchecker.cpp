#include <algorithm>
#include <cctype>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using std::string, std::vector;

typedef std::unordered_set<string> unique_set;
typedef std::unordered_map<string, string> dict;

class Solution {
private:
  string vowelize(const string &word) {
    string result = word;
    for (char &c : result) {
      char ch = std::tolower(c);
      if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
        c = 'a';
      } else {
        c = ch;
      }
    }

    return result;
  }

  string lowerize(const string &word) {
    string result;
    result.resize(word.size());

    std::transform(word.begin(), word.end(), result.begin(),
                   [](char ch) { return std::tolower(ch); });
    return result;
  }

public:
  vector<string> spellchecker(vector<string> &wordlist,
                              vector<string> &queries) {
    unique_set exact;
    dict lower;
    dict vowel;

    for (const string &word : wordlist) {
      if (!exact.count(word)) {
        exact.emplace(word);
      }

      string lowered = lowerize(word);
      if (!lower.count(lowered)) {
        lower.emplace(lowered, word);
      }

      string vowelled = vowelize(word);
      if (!vowel.count(vowelled)) {
        vowel.emplace(vowelled, word);
      }
    }

    vector<string> result;
    result.resize(queries.size());

    std::transform(
        queries.begin(), queries.end(), result.begin(),
        [&exact, &lower, &vowel, this](const string &query) -> string {
          if (exact.count(query)) {
            return query;
          }

          string lowered = this->lowerize(query);
          if (lower.count(lowered)) {
            return lower[lowered];
          }

          string vowelled = this->vowelize(query);
          if (vowel.count(vowelled)) {
            return vowel[vowelled];
          }

          return "";
        });

    return result;
  }
};